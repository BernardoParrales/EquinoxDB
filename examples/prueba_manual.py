"""
Prueba manual interactiva de EquinoxDB
Ejecuta: python3 examples/prueba_manual.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from equinoxdb import BaseDatos, Coleccion

print("=" * 60)
print("PRUEBA MANUAL DE EQUINOXDB")
print("=" * 60)

# 1. Crear instancia de base de datos
print("\n1. Creando instancia de BaseDatos...")
db = BaseDatos()
print("   ✓ BaseDatos creada")

# 2. Crear una colección
print("\n2. Creando colección 'usuarios'...")
resultado = db.crearColeccion("usuarios")
print(f"   {resultado}")

# 3. Insertar registros
print("\n3. Insertando registros...")
col = Coleccion("usuarios", [])

usuarios = [
    {"id": 1, "nombre": "Ana García", "edad": 28, "ciudad": "Madrid"},
    {"id": 2, "nombre": "Carlos López", "edad": 35, "ciudad": "Barcelona"},
    {"id": 3, "nombre": "María Rodríguez", "edad": 42, "ciudad": "Valencia"},
]

for usuario in usuarios:
    resultado = col.insertarRegistro(usuario)
    print(f"   ✓ {usuario['nombre']} - {resultado}")

# 4. Consultar todos los registros
print("\n4. Consultando todos los registros...")
datos = db.consultarColeccion("usuarios")
print(f"   Total de registros: {len(datos)}")
for i, usuario in enumerate(datos):
    print(f"   [{i}] {usuario['nombre']} - {usuario['edad']} años - {usuario['ciudad']}")

# 5. Leer un registro específico
print("\n5. Leyendo registro específico (índice 1)...")
col2 = Coleccion("usuarios", datos)
registro = col2.visualizarRegistro(1)
print(f"   Registro: {registro}")

# 6. Actualizar un registro
print("\n6. Actualizando registro (índice 0)...")
usuario_actualizado = {"id": 1, "nombre": "Ana García Pérez", "edad": 29, "ciudad": "Madrid"}
col2.actualizarRegistro(0, usuario_actualizado)
print(f"   ✓ Registro actualizado")

# Verificar actualización
datos_actualizados = db.consultarColeccion("usuarios")
print(f"   Nuevo valor: {datos_actualizados[0]['nombre']}")

# 7. Eliminar un registro
print("\n7. Eliminando registro (índice 2)...")
col3 = Coleccion("usuarios", datos_actualizados)
resultado = col3.eliminarRegistro(2)
print(f"   {resultado}")

# Verificar eliminación
datos_finales = db.consultarColeccion("usuarios")
print(f"   Registros restantes: {len(datos_finales)}")

# 8. Listar todas las colecciones
print("\n8. Listando todas las colecciones...")
colecciones = db.consultarNombreArchivosColecciones()
print(f"   Colecciones encontradas: {colecciones}")

# 9. Limpiar (opcional)
print("\n9. ¿Deseas eliminar la colección de prueba? (s/n): ", end="")
respuesta = input().strip().lower()
if respuesta == 's':
    resultado = db.eliminarColeccion("usuarios")
    print(f"   {resultado}")
else:
    print("   Colección 'usuarios' conservada en ./colecciones/usuarios.json")

print("\n" + "=" * 60)
print("PRUEBA MANUAL COMPLETADA")
print("=" * 60)
