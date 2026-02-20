def add_foreign_keys(columns):

    if not columns:
        print("Primero debes crear columnas.")
        return columns

    while True:
        print("\nColumnas disponibles para FOREIGN KEY:")
        for col in columns:
            print(f"- {col['name']}")

        fk_column = input(
            "\nDigite la columna que será FOREIGN KEY (Enter para terminar): "
        )

        # Si presiona Enter → termina
        if fk_column == "":
            break

        valid_names = [col["name"] for col in columns]

        if fk_column not in valid_names:
            print("Columna no válida.")
            continue

        reference_table = input("Digite la tabla referenciada: ")
        reference_column = input("Digite la columna referenciada: ")

        if reference_table == "" or reference_column == "":
            print("Referencia inválida.")
            continue

        fk_line = f"FOREIGN KEY({fk_column}) REFERENCES {reference_table}({reference_column})"

        columns.append({
            "name": "__foreign_key__",
            "sql": fk_line
        })

        print("FOREIGN KEY agregada correctamente.")

    return columns

