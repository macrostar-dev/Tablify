⌨️ Tablify - Generador Interactivo de Esquemas SQL

⚠️ Nota de Prototipo: Tablify se encuentra actualmente en su fase v1 (Prueba de Concepto). El objetivo de esta versión es validar la lógica de generación de comandos y la estructura modular. Aunque genera código SQL funcional, se recomienda su uso principalmente para fines de aprendizaje, prototipado rápido y pruebas en entornos controlados.

Tablify es un proyecto personal diseñado para facilitar y agilizar la creación de tablas en bases de datos a través de un sistema interactivo por consola. El objetivo principal es simplificar el modelado de datos, permitiendo que cualquier persona con conocimientos básicos genere esquemas sólidos y profesionales sin enfrentarse a los errores típicos de sintaxis o lógica manual.

🌟 ¿Por qué usar Tablify?
Muchas veces, escribir un CREATE TABLE largo puede llevar a errores (olvidar una coma, escribir mal una restricción o usar un tipo de dato incorrecto). Tablify te guía paso a paso, preguntándote qué necesitas y validando tus respuestas en tiempo real para asegurar que el resultado final sea impecable.

🗺️ Hoja de Ruta (Fases de Desarrollo)
v1: El Motor de Comandos (Estado Actual)
Es el prototipo funcional enfocado en la lógica y estructura.
  Generación de Código: Crea la línea de comando exacta (la "sentencia") para introducir tu modelo en la base de datos.
  Asistente de Consola: Te pregunta nombres, tipos de datos y restricciones (NOT NULL, UNIQUE, DEFAULT, etc.) de forma ordenada.
  Seguridad: Valida que los nombres de tablas y columnas sean correctos para evitar errores en el motor SQL.

v2: Conectividad y Consultas
El paso hacia una herramienta de gestión activa.
  Conexión Directa: Capacidad de conectarse a la base de datos y ejecutar la creación de tablas automáticamente.
  Consultas Asistidas: Ayuda para generar comandos de búsqueda (SELECT) y manipulación de datos sin escribir código.

v3: Integración con Excel y Visualización
Enfocada en el manejo de datos a gran escala.
  Visualización: Ver tus tablas directamente en la consola de forma legible.
  Importación/Exportación: Posibilidad de cargar datos desde Excel a la base de datos y extraer la base de datos completa a un archivo Excel para respaldos.

🛠️ Cómo funciona la v1
El proyecto es modular, lo que facilita que en el futuro se adapte a otros motores como MySQL o MariaDB. Actualmente cuenta con módulos para:
  Tipos de Datos: INTEGER, TEXT, REAL (decimales) y BLOB (binarios).
  Integridad: Gestión asistida de PRIMARY KEY y FOREIGN KEY.
  Validación: Uso de expresiones regulares para garantizar que cada entrada sea válida.

Instrucciones rápidas:
Ejecuta python main.py.
  Sigue las instrucciones para nombrar tu tabla y añadir columnas.
  Al terminar, copia la línea de comando generada y pégala en tu gestor de base de datos.

