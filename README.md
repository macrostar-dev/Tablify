# ⌨️ Tablify - Gestor Interactivo de Estructuras SQL

> [!IMPORTANT]
> **NOTA DE PROTOTIPO (v1):** Este proyecto es actualmente un **modelo de prueba** y una "Prueba de Concepto". 
> Su función principal es validar la lógica de generación de comandos y la estructura modular del sistema.
> 
> * **Motor Actual:** Optimizado exclusivamente para **SQLite**.
> * **Estado:** Estable para generación de sintaxis y tipos de datos de SQLite.
> * **Uso recomendado:** Aprendizaje, diseño rápido de esquemas y entornos de prueba controlados.

---

## 🌟 Sobre el Proyecto
**Tablify** es un proyecto personal diseñado para facilitar y agilizar la generación de tablas de bases de datos mediante un sistema interactivo por consola. Su objetivo es simplificar la creación de esquemas, permitiendo que el usuario con conocimientos básicos genere esquemas sólidos sin enfrentarse a los problemas comunes de sintaxis manual.

## 🗺️ Hoja de Ruta (Roadmap)

* **v1 (Actual):** Motor de generación de sintaxis centrado en **SQLite**.
* **v2 (Próximamente):** Conectividad directa a base de datos, ejecución de comandos y motor de consultas asistido.
* **v3 (Futuro):** Visualización de tablas e integración para importar/exportar datos con Excel.

## 🛠️ Especificaciones de la v1 (SQLite)
El sistema ya maneja las particularidades de SQLite, como:
* **Tipos de datos nativos:** INTEGER, TEXT, REAL y BLOB.
* **Cotejamientos:** Soporte para `COLLATE NOCASE`.
* **Seguridad:** Escapado de comillas simples y validación de hexadecimales para BLOBs.
* **Relaciones:** Integridad referencial mediante `PRIMARY KEY` y `FOREIGN KEY`.
