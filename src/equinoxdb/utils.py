import pathlib
RUTA_COLECCIONES = str(pathlib.Path().absolute()) + f"/colecciones"
RUTA_ADSOLUTA = str(pathlib.Path().absolute())

def titulo(texto):
    print(f"########## {texto} ##########")
    
def literal(literales):
    for literal in literales:
        indice = (literales.index(literal)) + 1
        print(f"{indice}. {literal}")
        
def leerEntradas(tipo, mensaje = "> "):
    valor = None
    while valor == None:
        try:
            if tipo == "int":
                valor = int(input(mensaje)) 
            elif tipo == "str":
                valor = input(mensaje)
        except ValueError:
            print("Solo se permite valores numericos")
    return valor


import datetime 
def obtenerDatatime():
    fecha_completa = datetime.datetime.now()
    return fecha_completa


def registrarLog(evento):
    # Obtener la ruta del archivo del registro del sistema
    ruta_log = RUTA_ADSOLUTA + "/log.txt"
    # Abrir el archivo de registro del sistema con el parametro "a+" (append and read - añadir y leer)
    with open(ruta_log, "a+") as archivo:
        # Escribir en el archivo del registro
        archivo.write(f"\n{obtenerDatatime()}:{evento}")
        
import os
def encontrarRuta(nombreColeccion):
    ruta_coleccion = RUTA_COLECCIONES + f"/{nombreColeccion}.json"
    existe_coleccion = os.path.exists(ruta_coleccion)
    return ruta_coleccion, existe_coleccion


        
    