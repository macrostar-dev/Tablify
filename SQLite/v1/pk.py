def add_primary_keys(columns):

    if not columns:
        return columns

    while True:
        print("\nColumnas disponibles:")
        for col in columns:
            print(f"- {col['name']}")

        pk_input = input(
            "\nDigite columnas para PRIMARY KEY separadas por coma (Enter para terminar): "
        )

        # Si presiona Enter sin escribir nada → termina
        if pk_input == "":
            break

        pk_columns = [col.strip() for col in pk_input.split(",")]

        # Validar nombres existentes
        valid_names = [col["name"] for col in columns]
        selected = [name for name in pk_columns if name in valid_names]

        if not selected:
            print("Ninguna columna válida.")
            continue

        pk_line = f"PRIMARY KEY({', '.join(selected)})"

        columns.append({
            "name": "__primary_key__",
            "sql": pk_line
        })

        print("PRIMARY KEY agregada correctamente.")

    return columns

