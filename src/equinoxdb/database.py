# Clase de base de datos

import os
import pathlib
from utilidades import *
import json

COD = {"Inicializar": "Se creo el directorio colecciones",
       "Comprobar Coleccion": "Se comprobo el directorio colecciones, el cual ya existe.",
       "Crear coleccion": "Se creo la coleccion con exito.",
       "Coleccion Existe": "La colección ya existe.",
       "Eliminar coleccion": "Se eliminó la coleccion con exito.",
       "Coleccion no existe": "La coleccion no existe.",
       "Coleccion encontrada": "La coleccion fue encontrada con exito",
       "Archivo no existe": "El archivo de la coleccion no existe.",
       "Datos JSON invalidados": "El archivo de la coleccion no contiene datos JSON válidos.",
       }

class BaseDatos:
    
    # Atributos de la clase
    __nombreDB = ""
    __colecciones = []
    
    
    # METODOS DE LA CLASE
    
    # Constructor
    def __init__(self):
        registrarLog("Se inicializo la base de datos") # Registrar en el log la inicialización de la bd
        if not os.path.isdir("./colecciones"): # Comprobar si existe el directorio coleccion
            os.mkdir("./colecciones") # Crear el directorio coleccion
            registrarLog(COD["Inicializar"])
        else:
            registrarLog(COD["Comprobar Coleccion"])
    
    def crearColeccion(self, nombreColeccion):
        # Encontrar la ruta
        ruta_coleccion, existe_coleccion = encontrarRuta(nombreColeccion)
        
        # Comprobar la existencia de una coleccion
        if existe_coleccion:
            registrarLog(COD["Coleccion Existe"])
            return COD["Coleccion Existe"]
        else:
            # Crear la colección
            with open(ruta_coleccion, "w") as archivo_coleccion:
                archivo_coleccion.write("")
                mensaje = COD["Crear coleccion"]+f" Coleccion: {nombreColeccion}, en la ruta '{ruta_coleccion}'"
                registrarLog(mensaje)
                return mensaje
            
    def eliminarColeccion(self, nombreColeccion):
        # Encontrar la ruta
        ruta_coleccion, existe_coleccion = encontrarRuta(nombreColeccion)
        
        # Eliminar el archivo de la coleccion
        if existe_coleccion:
            os.remove(ruta_coleccion)
            mensaje = COD["Eliminar coleccion"]+f" coleccion: {nombreColeccion}"
            registrarLog(mensaje)
            return mensaje
        else:
            # Mensaje de error al no encontar la coleccion a borrar
            mensaje = COD["Coleccion no existe"]
            registrarLog(mensaje)
            return mensaje
        
    def consultarColeccion(self, nombreColeccion):
        # Encontrar la ruta
        ruta_coleccion, existe_coleccion = encontrarRuta(nombreColeccion)
        
        # Retornar la coleccion
        if existe_coleccion:
            try:    
                with open(ruta_coleccion, "r") as archivo_coleccion:
                    coleccion = json.load(archivo_coleccion)                    
                    mensaje = COD["Coleccion encontrada"]+f" coleccion: {nombreColeccion}"
                    registrarLog(mensaje)
                    return coleccion
                
            except FileNotFoundError:
                mensaje = COD["Archivo no existe"]
                registrarLog(mensaje)
                return mensaje
            
            except json.decoder.JSONDecodeError:
                mensaje = COD["Datos JSON invalidados"]
                registrarLog(mensaje)
                return mensaje
        else:
            # Mensaje de error al no encontar la coleccion a borrar
            mensaje = COD["Coleccion no existe"]
            registrarLog(mensaje)
            return mensaje
        
    def consultarNombreArchivosColecciones(self):
        ruta = str(pathlib.Path().absolute()) + f"/colecciones"
        nombre_archivo_colecciones = os.listdir(ruta)
        return nombre_archivo_colecciones
    
    def consultarColecciones(self):
        nombre_colecciones = self.consultarNombreArchivosColecciones()
        for nombre_coleccion in nombre_colecciones:
            nombre_archivo, extension = os.path.splitext(nombre_coleccion)
            if extension == ".json":
                self.__colecciones.append({nombre_archivo:self.consultarColeccion(nombre_archivo)})
        return self.__colecciones
        

'''
db = BaseDatos()
#print(db.consultarNombreArchivosColecciones())
coleccion= db.consultarColeccion("Animales")
print(coleccion)
print(db.consultarNombreArchivosColecciones())
print(db.consultarColecciones())
r = db.crearColeccion("Animales")
print(r)
r = db.crearColeccion("Programadores")
print(r)
r = db.crearColeccion("Casas")
print(r)
r = db.eliminarColeccion("Animales")
print(r)
'''

#ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#print(ruta)
#archivo = open(ruta, "a+")

