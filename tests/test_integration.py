"""
Integration tests for EquinoxDB CRUD operations
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from equinoxdb import BaseDatos, Coleccion


def test_crud_completo():
    """Test complete CRUD cycle"""
    print("Test: CRUD completo...")
    db = BaseDatos()
    
    # CREATE collection
    db.crearColeccion("test_crud")
    
    # CREATE records
    col = Coleccion("test_crud", [])
    col.insertarRegistro({"id": 1, "nombre": "Ana", "edad": 25})
    col.insertarRegistro({"id": 2, "nombre": "Bob", "edad": 30})
    col.insertarRegistro({"id": 3, "nombre": "Carlos", "edad": 35})
    
    # READ records
    datos = db.consultarColeccion("test_crud")
    assert len(datos) == 3
    print(f"  ✓ 3 registros insertados")
    
    # READ single record
    col2 = Coleccion("test_crud", datos)
    registro = col2.visualizarRegistro(0)
    assert registro["nombre"] == "Ana"
    print(f"  ✓ Registro leído: {registro['nombre']}")
    
    # UPDATE record
    col2.actualizarRegistro(0, {"id": 1, "nombre": "Ana María", "edad": 26})
    datos_actualizados = db.consultarColeccion("test_crud")
    assert datos_actualizados[0]["nombre"] == "Ana María"
    print(f"  ✓ Registro actualizado")
    
    # DELETE record
    col3 = Coleccion("test_crud", datos_actualizados)
    col3.eliminarRegistro(1)
    datos_finales = db.consultarColeccion("test_crud")
    assert len(datos_finales) == 2
    print(f"  ✓ Registro eliminado, quedan {len(datos_finales)}")
    
    # DELETE collection
    db.eliminarColeccion("test_crud")
    print("✓ CRUD completo exitoso")


def test_multiples_colecciones():
    """Test multiple collections"""
    print("\nTest: Múltiples colecciones...")
    db = BaseDatos()
    
    # Create multiple collections
    db.crearColeccion("usuarios")
    db.crearColeccion("productos")
    db.crearColeccion("pedidos")
    
    # List collections
    nombres = db.consultarNombreArchivosColecciones()
    assert len(nombres) >= 3
    print(f"  ✓ {len(nombres)} colecciones creadas")
    
    # Cleanup
    db.eliminarColeccion("usuarios")
    db.eliminarColeccion("productos")
    db.eliminarColeccion("pedidos")
    print("✓ Múltiples colecciones manejadas correctamente")


def test_json_vacio():
    """Test handling empty JSON"""
    print("\nTest: JSON vacío...")
    db = BaseDatos()
    
    # Create empty collection
    db.crearColeccion("test_vacio")
    
    # Try to insert in empty collection
    col = Coleccion("test_vacio", [])
    result = col.insertarRegistro({"test": "data"})
    assert "exitosamente" in result
    print("  ✓ Inserción en colección vacía manejada")
    
    # Cleanup
    db.eliminarColeccion("test_vacio")
    print("✓ JSON vacío manejado correctamente")


def test_datos_complejos():
    """Test complex data structures"""
    print("\nTest: Datos complejos...")
    db = BaseDatos()
    
    db.crearColeccion("test_complejo")
    
    # Insert complex record
    registro_complejo = {
        "id": 1,
        "nombre": "Usuario Test",
        "datos": {
            "email": "test@example.com",
            "telefono": "123456789"
        },
        "tags": ["python", "database", "nosql"],
        "activo": True,
        "puntos": 99.5
    }
    
    col = Coleccion("test_complejo", [])
    col.insertarRegistro(registro_complejo)
    
    # Verify
    datos = db.consultarColeccion("test_complejo")
    assert datos[0]["datos"]["email"] == "test@example.com"
    assert len(datos[0]["tags"]) == 3
    print("  ✓ Datos complejos almacenados correctamente")
    
    # Cleanup
    db.eliminarColeccion("test_complejo")
    print("✓ Datos complejos manejados correctamente")


def run_integration_tests():
    """Run all integration tests"""
    print("=" * 50)
    print("Pruebas de Integración - EquinoxDB")
    print("=" * 50)
    
    tests = [
        test_crud_completo,
        test_multiples_colecciones,
        test_json_vacio,
        test_datos_complejos,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ Test falló: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Resultados: {passed} pasaron, {failed} fallaron")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    success = run_integration_tests()
    sys.exit(0 if success else 1)
