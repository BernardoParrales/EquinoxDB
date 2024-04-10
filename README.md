# EquinoxDB

EquinoxDB es un Sistema Gestor de Base de Datos (SGBD) desarrollado en Python para el almacenamiento y gestión de datos no relacionales, el cual funciona como un servidor propio e independiente, es decir se incluye la base de datos y el motor dentro del programa en el que se implemente, similar a SQLite.
Este SGBD permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en colecciones de datos almacenadas en archivos JSON.

## Características

- Soporte para operaciones CRUD en colecciones de datos JSON.
- Tolerancia a fallos al insertar registros en colecciones vacías.
- Acceso a valores mediante claves sin utilizar bucles.

## Estructura del Proyecto (Aun en desarrollo)

El proyecto está estructurado de la siguiente manera: 

- `BaseDatos.py`: Contiene la implementación de la clase BaseDatos para gestionar las colecciones de datos.
- `Coleccion.py`: Contiene la implementación de la clase Coleccion para representar las colecciones de datos.
- `Consola.py`: Contiene la implementación de la clase Consola para interactuar con el usuario.
- `README.md`: Este archivo que estás leyendo.

## Uso

Para utilizar EquinoxDB en tu proyecto, sigue estos pasos:

1. Descarga o clona el repositorio en tu sistema.
2. Importa las clases necesarias en tu código.
3. Crea una instancia de la clase `BaseDatos` y comienza a gestionar tus colecciones de datos.

## Ejemplo de Uso

Aquí tienes un ejemplo básico de cómo puedes utilizar EquinoxDB en tu proyecto:

```python
from BaseDatos import BaseDatos

# Crear una instancia de BaseDatos
db = BaseDatos()

# Crear una nueva colección
db.crearColeccion("personas")

# Insertar un registro en la colección "personas"
registro = {"nombre": "Juan", "edad": 30, "ciudad": "Ciudad de México"}
db.insertarRegistro("personas", registro)

# Consultar la colección "personas"
coleccion = db.consultarColeccion("personas")
print(coleccion)
```

## Contribuir
Si deseas contribuir a EquinoxDB, ¡eres bienvenido! Puedes abrir un problema para informar sobre errores o sugerir nuevas características. Si deseas enviar una corrección o implementar una nueva función, envía una solicitud de extracción. Asegúrate de seguir las directrices de contribución del proyecto.

### Licencia
Este proyecto está bajo la licencia de código abierto.
