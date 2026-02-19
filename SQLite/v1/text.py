import re

def is_valid_identifier(name):
    """
    Valida nombre SQL: empieza con letra o _
    y solo contiene letras, números o _
    """
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None


def is_valid_integer(value):
    """
    Valida entero positivo (para LENGTH).
    """
    return re.match(r'^\d+$', value) is not None


def escape_quotes(text):
    """
    Escapa comillas simples para evitar romper SQL.
    """
    return text.replace("'", "''")


def generate_text_column_sql():
    """
    Genera definición SQL para columna TEXT
    con validaciones para evitar sintaxis inválida.
    """

    TEXT_MODEL = {
        "base": "TEXT",
        "constraints": {
            1: {"key": "not_null", "label": "No permitir NULL", "sql": "NOT NULL", "unique": True},
            2: {"key": "unique", "label": "Valor único", "sql": "UNIQUE", "unique": True},
            3: {"key": "default", "label": "Valor por defecto", "sql": "DEFAULT '{value}'", "unique": True},
            4: {"key": "collate", "label": "Comparación sin mayúsculas (NOCASE)", "sql": "COLLATE NOCASE", "unique": True},
            5: {"key": "check", "label": "Condición CHECK", "sql": "CHECK({check})", "unique": False},
        }
    }

    TEXT_CHECKS = {
        1: {"label": "Longitud mínima", "sql": 'LENGTH("{col}") >= {value}'},
        2: {"label": "Longitud máxima", "sql": 'LENGTH("{col}") <= {value}'},
        3: {"label": "Longitud exacta", "sql": 'LENGTH("{col}") = {value}'},
    }

    # --- Validar nombre ---
    while True:
        name = input("Digite el nombre de la columna: ")
        if is_valid_identifier(name):
            break
        print("⚠️ Nombre inválido. Use solo letras, números y _ (no puede iniciar con número).")

    column_parts = [name, TEXT_MODEL["base"]]
    used_constraints = set()

    while True:
        print("\n--- Restricciones TEXT disponibles ---")
        for num, data in TEXT_MODEL["constraints"].items():
            status = ""
            if data["unique"] and data["key"] in used_constraints:
                status = " [Ya aplicado]"
            print(f"{num}. {data['label']}{status}")

        choice = input("Selecciona una opción (ENTER para finalizar): ")
        if not choice:
            break

        try:
            choice_idx = int(choice)
            constraint = TEXT_MODEL["constraints"][choice_idx]
        except (ValueError, KeyError):
            print("⚠️ Opción no válida.")
            continue

        if constraint["unique"] and constraint["key"] in used_constraints:
            print("⚠️ Esta restricción ya fue agregada.")
            continue

        sql_piece = constraint["sql"]

        # DEFAULT
        if "{value}" in sql_piece:
            val = input("Texto por defecto: ")
            val = escape_quotes(val)
            sql_piece = sql_piece.format(value=val)

        # CHECK LENGTH
        elif "{check}" in sql_piece:
            print("\n--- Opciones de validación de texto (LENGTH) ---")
            for num, data in TEXT_CHECKS.items():
                print(f"{num}. {data['label']}")

            try:
                check_idx = int(input("Selecciona la opción: "))
                check_template = TEXT_CHECKS[check_idx]["sql"]
            except (ValueError, KeyError):
                print("⚠️ Opción inválida.")
                continue

            while True:
                val = input("Cantidad de caracteres: ")
                if is_valid_integer(val):
                    break
                print("⚠️ Debe ser un número entero positivo.")

            check_sql = check_template.format(col=name, value=val)
            sql_piece = sql_piece.format(check=check_sql)

        column_parts.append(sql_piece)
        used_constraints.add(constraint["key"])

    final_sql = " ".join(column_parts)
    print(f"\n✅ Definición TEXT generada: {final_sql}")

    # 🔥 Retornamos el diccionario para que xxx.py no falle
    return {"name": name, "sql": final_sql}


if __name__ == "__main__":
    resultado = generate_text_column_sql()
    print(f"Resultado: {resultado}")