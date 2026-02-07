#!/usr/bin/env python3
"""
Run all tests for EquinoxDB
"""
import sys
import os

# Add tests directory to path
sys.path.insert(0, os.path.dirname(__file__))

from test_basic import run_all_tests
from test_integration import run_integration_tests


def main():
    print("\n" + "=" * 60)
    print(" " * 15 + "EQUINOXDB TEST SUITE")
    print("=" * 60 + "\n")
    
    # Run basic tests
    print("📋 PARTE 1: Pruebas Básicas")
    print("-" * 60)
    basic_success = run_all_tests()
    
    print("\n")
    
    # Run integration tests
    print("📋 PARTE 2: Pruebas de Integración")
    print("-" * 60)
    integration_success = run_integration_tests()
    
    # Summary
    print("\n" + "=" * 60)
    print(" " * 20 + "RESUMEN FINAL")
    print("=" * 60)
    
    if basic_success and integration_success:
        print("✅ TODAS LAS PRUEBAS PASARON")
        print(f"   - Pruebas básicas: ✓")
        print(f"   - Pruebas de integración: ✓")
        return 0
    else:
        print("❌ ALGUNAS PRUEBAS FALLARON")
        if not basic_success:
            print(f"   - Pruebas básicas: ✗")
        if not integration_success:
            print(f"   - Pruebas de integración: ✗")
        return 1


if __name__ == "__main__":
    sys.exit(main())
