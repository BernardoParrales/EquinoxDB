# Clase Colección

import json
from .utils import encontrarRuta, registrarLog
from . import constants as env


class Coleccion():
    __nombreColeccion = ""
    __registros = []
    
    def __init__(self, nombreColeccion, registros):
        self.__nombreColeccion = nombreColeccion
        self.__registros = registros
        
    def insertarRegistro(self, registro):
        ruta, validar = encontrarRuta(self.__nombreColeccion)
        # La colección existe, 
        if validar:
            try:
                with open(ruta, 'r') as archivo:
                    # Cargar contenido actual
                    contenido_actual = json.load(archivo)
                    registrarLog(f"Se ha cargado el archivo JSON de la coleccion {self.__nombreColeccion}")
            except json.decoder.JSONDecodeError:
                # Si el archivo está vacío o no es un JSON válido, inicializar contenido actual como una lista vacía
                contenido_actual = []
                registrarLog(f"El archivo JSON de la coleccion {self.__nombreColeccion} esta vacio o no es un JSON valido, se inicializara como una lista vacía.")
            
            # Agregar el nuevo registro
            contenido_actual.append(registro)
                        
            # Escribir contenido actualizado de vuelta al archivo
            with open(ruta, 'w') as archivo:
                json.dump(contenido_actual, archivo, indent=4)
                registrarLog(f"Se agrego un nuevo registro a la coleccion {self.__nombreColeccion}.")
            
            return ("Registro insertado exitosamente.")
            
        else:
            registrarLog(env.COD["Coleccion no existe"])
            print("La coleccion no se encuentra")
        
    def visualizarRegistro(self, clave):
        ruta, validar = encontrarRuta(self.__nombreColeccion)
        # La colección existe, 
        if validar:
            try:
                with open(ruta, 'r') as archivo:
                    # Cargar contenido actual
                    contenido_actual = json.load(archivo)
            except json.decoder.JSONDecodeError:
                # Si el archivo está vacío o no es un JSON válido, inicializar contenido actual como una lista vacía
                print("La coleccion no se encuentra.")
            # Busqueda directa utilizando indexación directa
            return contenido_actual[clave]
        else:
            registrarLog(env.COD["Coleccion no existe"])
            print("La coleccion no se encuentra")
        
        
    def visualizarRegistros(self):
        return self.__registros
      
    
    def actualizarRegistro(self, clave, registro):
        ruta, validar = encontrarRuta(self.__nombreColeccion)
        # La colección existe, 
        if validar:
            
            # Traer la coleccion actual
            try:
                with open(ruta, 'r') as archivo:
                    # Cargar contenido actual
                    coleccion_actual = json.load(archivo)
                    registrarLog(f"Se ha cargado el archivo JSON de la coleccion {self.__nombreColeccion}")
            except json.decoder.JSONDecodeError:
                # Si el archivo está vacío o no es un JSON válido, inicializar contenido actual como una lista vacía
                registrarLog(f"El archivo JSON de la coleccion {self.__nombreColeccion} esta vacio o no es un JSON valido, se inicializara como una lista vacía.")
            
            registro_actual = self.visualizarRegistro(clave)
            if registro_actual != None:
                registro_actual = registro # Buscar el registro
                coleccion_actual[clave] = registro_actual # Agregar el nuevo registro
                        
            # Escribir contenido actualizado de vuelta al archivo
            with open(ruta, 'w') as archivo:
                json.dump(coleccion_actual, archivo, indent=4)
                registrarLog(f"Se agrego un nuevo registro a la coleccion {self.__nombreColeccion}.")
            return ("Registro insertado exitosamente.")
            
        else:
            registrarLog(env.COD["Coleccion no existe"])
            print("La coleccion no se encuentra")
        
    def eliminarRegistro(self, clave):
        ruta, validar = encontrarRuta(self.__nombreColeccion)
        # La colección existe, 
        if validar:
            
            # Traer la coleccion actual
            try:
                with open(ruta, 'r') as archivo:
                    # Cargar contenido actual
                    coleccion_actual = json.load(archivo)
                    registrarLog(f"Se ha cargado el archivo JSON de la coleccion {self.__nombreColeccion}")
            except json.decoder.JSONDecodeError:
                # Si el archivo está vacío o no es un JSON válido, inicializar contenido actual como una lista vacía
                registrarLog(f"El archivo JSON de la coleccion {self.__nombreColeccion} esta vacio o no es un JSON valido, se inicializara como una lista vacía.")
            
            registro_actual = self.visualizarRegistro(clave)
            if registro_actual != None:
                coleccion_actual.remove(coleccion_actual[clave])
                        
            # Escribir contenido actualizado de vuelta al archivo
            with open(ruta, 'w') as archivo:
                json.dump(coleccion_actual, archivo, indent=4)
                registrarLog(f"Se elimino un registro de la coleccion {self.__nombreColeccion}.")
            return ("Registro eliminado exitosamente.")
            
        else:
            registrarLog(env.COD["Coleccion no existe"])
            print("La coleccion no se encuentra")
