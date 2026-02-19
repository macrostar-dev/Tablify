# ⌨️ Tablify - Gestor Interactivo de Estructuras SQL

> [!IMPORTANT]
> **NOTA DE PROTOTIPO (v1):** Este proyecto es actualmente un **modelo de prueba** y una "Prueba de Concepto". 
> Su función principal es validar la lógica de generación de comandos y la estructura modular del sistema para evitar errores de sintaxis manuales.

Tablify es un proyecto personal diseñado para facilitar y agilizar la generación de tablas de bases de datos mediante un sistema interactivo por consola. Su objetivo es simplificar la creación de esquemas sólidos, permitiendo que usuarios con conocimientos básicos obtengan comandos SQL profesionales sin lidiar con los errores comunes de escritura.

## 🗺️ Hoja de Ruta (Roadmap)

* **v1 (Actual):** Motor de generación de sintaxis (Línea de comando).
* **v2 (Próximamente):** Conectividad directa a DB y motor de consultas asistido.
* **v3 (Futuro):** Visualización de datos e integración (Importar/Exportar) con Excel.

## 🛠️ Características Técnicas
* **Modularidad:** Código dividido por tipos de datos (INTEGER, TEXT, BLOB, REAL).
* **Validación con RegEx:** Seguridad en nombres de identificadores y tipos de valores.
* **Gestión de Restricciones:** Control inteligente de `NOT NULL`, `UNIQUE` y `CHECK`.
* **Relaciones:** Soporte para `PRIMARY KEY` compuestas y `FOREIGN KEY`.

