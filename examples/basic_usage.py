"""
Basic usage example for EquinoxDB
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from equinoxdb import BaseDatos

# Create database instance
db = BaseDatos()

# Create a new collection
print("Creating collection 'personas'...")
result = db.crearColeccion("personas")
print(result)

# Query the collection
print("\nQuerying collection 'personas'...")
coleccion = db.consultarColeccion("personas")
print(coleccion)

# List all collections
print("\nListing all collections...")
nombres = db.consultarNombreArchivosColecciones()
print(f"Collections: {nombres}")
