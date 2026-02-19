import re

def is_valid_identifier(name):
    """
    Valida nombre SQL: empieza con letra o _
    y solo contiene letras, números o _
    """
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None


def is_valid_integer(value):
    """
    Valida entero positivo.
    """
    return re.match(r'^\d+$', value) is not None


def is_valid_hex(value):
    """
    Valida que el valor sea hexadecimal válido.
    """
    return re.match(r'^[0-9A-Fa-f]+$', value) is not None


def generate_blob_column_sql():
    """
    Genera una sentencia SQL para una columna tipo BLOB
    con validaciones de seguridad.
    """

    BLOB_MODEL = {
        "base": "BLOB",
        "constraints": {
            1: {"key": "not_null", "label": "No permitir NULL", "sql": "NOT NULL", "unique": True},
            2: {"key": "unique", "label": "Valor único", "sql": "UNIQUE", "unique": True},
            3: {"key": "default", "label": "Valor por defecto (hex)", "sql": "DEFAULT x'{value}'", "unique": True},
            4: {"key": "check", "label": "Condición CHECK", "sql": "CHECK({check})", "unique": False}
        }
    }

    BLOB_CHECKS = {
        1: {"label": "Limitar tamaño máximo (bytes)", "sql": 'length("{col}") <= {value}'},
        2: {"label": "Limitar tamaño mínimo (bytes)", "sql": 'length("{col}") >= {value}'},
        3: {"label": "Tamaño exacto (bytes)", "sql": 'length("{col}") = {value}'},
        4: {"label": "No permitir BLOB vacío", "sql": 'length("{col}") > 0'},
        5: {"label": "Forzar tipo BLOB", "sql": 'typeof("{col}") = \'blob\''},
        6: {"label": "Comparar con valor hexadecimal específico", "sql": '"{col}" = x\'{value}\''}
    }

    # --- Validar nombre ---
    while True:
        name = input("Digite el nombre de la columna: ")
        if is_valid_identifier(name):
            break
        print("⚠️ Nombre inválido. Use solo letras, números y _ (no puede iniciar con número).")

    column_parts = [name, BLOB_MODEL["base"]]
    used_constraints = set()

    while True:
        print("\n--- Restricciones BLOB disponibles ---")
        for num, data in BLOB_MODEL["constraints"].items():
            status = ""
            if data["unique"] and data["key"] in used_constraints:
                status = " [Ya aplicado]"
            print(f"{num}. {data['label']}{status}")

        choice = input("Selecciona una opción (ENTER para finalizar): ")
        if not choice:
            break

        try:
            choice_idx = int(choice)
            constraint = BLOB_MODEL["constraints"][choice_idx]
        except (ValueError, KeyError):
            print("⚠️ Opción no válida.")
            continue

        if constraint["unique"] and constraint["key"] in used_constraints:
            print("⚠️ Esta restricción ya fue agregada.")
            continue

        sql_piece = constraint["sql"]

        # DEFAULT HEX
        if "{value}" in sql_piece and "{check}" not in sql_piece:
            while True:
                val = input("Valor hexadecimal (sin x''): ")
                if is_valid_hex(val):
                    break
                print("⚠️ Debe contener solo caracteres hexadecimales (0-9, A-F).")

            sql_piece = sql_piece.format(value=val)

        # CHECK
        elif "{check}" in sql_piece:
            print("\n--- Opciones de validación CHECK ---")
            for num, data in BLOB_CHECKS.items():
                print(f"{num}. {data['label']}")

            try:
                check_idx = int(input("Selecciona la opción: "))
                check_template = BLOB_CHECKS[check_idx]["sql"]
            except (ValueError, KeyError):
                print("⚠️ Opción inválida.")
                continue

            if "{value}" in check_template:
                if "length" in check_template:
                    while True:
                        val = input("Cantidad de bytes: ")
                        if is_valid_integer(val):
                            break
                        print("⚠️ Debe ser un número entero positivo.")
                else:
                    while True:
                        val = input("Valor hexadecimal: ")
                        if is_valid_hex(val):
                            break
                        print("⚠️ Debe contener solo caracteres hexadecimales.")

                check_sql = check_template.format(col=name, value=val)
            else:
                check_sql = check_template.format(col=name)

            sql_piece = sql_piece.format(check=check_sql)

        column_parts.append(sql_piece)
        used_constraints.add(constraint["key"])

    final_sql = " ".join(column_parts)
    print(f"\n✅ Definición BLOB generada: {final_sql}")
    
    return {"name": name, "sql": final_sql}


if __name__ == "__main__":
    resultado = generate_blob_column_sql()
    print(f"Resultado: {resultado}")
