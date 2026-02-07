# Consola: Menu de opciones para la base de datos

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from equinoxdb.utils import titulo, literal, leerEntradas


op = None

literales = ["Crear colección", 
             "Crear registro", 
             "Ver registros", 
             "Ver registro", 
             "Actualizar registro",
             "Eliminar registro",
             "Cerrar"]


def mostrarOpciones():
    while True:
        titulo("EquinoxDB")
        literal(literales)
        op = leerEntradas("str")
        
        if op == "1":
            titulo(literales[0])
            op = leerEntradas("str")
            
            
        elif op == "2":
            titulo(literales[1])
            
        elif op == "3":
            titulo(literales[2])
            
        elif op == "4":
            titulo(literales[3])
            
        elif op == "5":
            titulo(literales[4])
            
        elif op == "6":
            titulo(literales[5])

        elif op == "7":
            break




        