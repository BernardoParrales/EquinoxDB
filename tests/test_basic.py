"""
Basic tests for EquinoxDB
"""
import sys
import os
import tempfile
import shutil

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from equinoxdb import BaseDatos, Coleccion


def test_crear_coleccion():
    """Test creating a collection"""
    print("Test: Crear colección...")
    db = BaseDatos()
    result = db.crearColeccion("test_personas")
    assert "Se creo la coleccion con exito" in result
    print("✓ Colección creada exitosamente")


def test_consultar_coleccion():
    """Test querying a collection"""
    print("\nTest: Consultar colección...")
    db = BaseDatos()
    coleccion = db.consultarColeccion("test_personas")
    assert isinstance(coleccion, (list, str))
    print(f"✓ Colección consultada: {type(coleccion)}")


def test_eliminar_coleccion():
    """Test deleting a collection"""
    print("\nTest: Eliminar colección...")
    db = BaseDatos()
    result = db.eliminarColeccion("test_personas")
    assert "Se eliminó la coleccion con exito" in result
    print("✓ Colección eliminada exitosamente")


def test_coleccion_no_existe():
    """Test querying non-existent collection"""
    print("\nTest: Colección no existe...")
    db = BaseDatos()
    result = db.consultarColeccion("coleccion_inexistente")
    assert "no existe" in result
    print("✓ Error manejado correctamente")


def test_listar_colecciones():
    """Test listing collections"""
    print("\nTest: Listar colecciones...")
    db = BaseDatos()
    nombres = db.consultarNombreArchivosColecciones()
    assert isinstance(nombres, list)
    print(f"✓ Colecciones encontradas: {len(nombres)}")


def test_insertar_registro():
    """Test inserting a record"""
    print("\nTest: Insertar registro...")
    db = BaseDatos()
    
    # Create collection
    db.crearColeccion("test_insert")
    
    # Get collection data
    datos = db.consultarColeccion("test_insert")
    if isinstance(datos, str):
        datos = []
    
    # Create Coleccion instance
    col = Coleccion("test_insert", datos)
    
    # Insert record
    registro = {"nombre": "Juan", "edad": 30}
    result = col.insertarRegistro(registro)
    assert "exitosamente" in result
    print("✓ Registro insertado")
    
    # Cleanup
    db.eliminarColeccion("test_insert")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Ejecutando pruebas de EquinoxDB")
    print("=" * 50)
    
    tests = [
        test_crear_coleccion,
        test_consultar_coleccion,
        test_listar_colecciones,
        test_insertar_registro,
        test_coleccion_no_existe,
        test_eliminar_coleccion,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ Test falló: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Resultados: {passed} pasaron, {failed} fallaron")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
