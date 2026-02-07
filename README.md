# EquinoxDB

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Lightweight embedded NoSQL database for Python

EquinoxDB is a simple, embedded NoSQL database management system (DBMS) developed in Python for storing and managing non-relational data. It functions as a self-contained, independent server, similar to SQLite, with the database and engine included within the program.

## ✨ Features

- 🚀 **Zero external dependencies** - Uses only Python standard library
- 📦 **Embedded database** - No server required, runs in your application
- 💾 **JSON-based storage** - Human-readable data format
- 🔍 **CRUD operations** - Create, Read, Update, Delete records
- 📝 **Simple API** - Intuitive and easy to use
- 🐍 **Pure Python** - 100% Python implementation
- 🛡️ **Fault tolerant** - Handles empty or invalid JSON files gracefully

## 📦 Installation

### From source

```bash
git clone https://github.com/BernardoParrales/EquinoxDB.git
cd EquinoxDB
pip install -e .
```

## 🚀 Quick Start

```python
from equinoxdb import BaseDatos

# Create database instance
db = BaseDatos()

# Create a new collection
db.crearColeccion("personas")

# Insert a record
registro = {"nombre": "Juan", "edad": 30, "ciudad": "Ciudad de México"}
db.insertarRegistro("personas", registro)

# Query the collection
coleccion = db.consultarColeccion("personas")
print(coleccion)
```

## 📚 Documentation

- [Getting Started](docs/getting-started.md)
- [API Reference](docs/api-reference.md)
- [Examples](examples/)

## 🗂️ Project Structure

```
EquinoxDB/
├── src/equinoxdb/      # Source code
├── tests/              # Test suite
├── examples/           # Usage examples
├── docs/               # Documentation
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Bernardo Parrales** - [@BernardoParrales](https://github.com/BernardoParrales)

## 🙏 Acknowledgments

- Inspired by SQLite's embedded database approach
- Built for small-scale Python applications that need simple data persistence
