import re

def is_valid_identifier(name):
    """
    Valida nombre SQL: empieza con letra o _
    y solo contiene letras, números o _
    """
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None


def is_valid_real(value):
    """
    Valida número REAL (entero o decimal, positivo o negativo).
    """
    return re.match(r'^-?\d+(\.\d+)?$', value) is not None


def generate_real_column_sql():
    """
    Genera la definición SQL de una columna REAL
    con validaciones de seguridad.
    """

    REAL_MODEL = {
        "base": "REAL",
        "constraints": {
            1: {"key": "not_null", "label": "No permitir NULL", "sql": "NOT NULL", "unique": True},
            2: {"key": "unique", "label": "Valor único", "sql": "UNIQUE", "unique": True},
            3: {"key": "default", "label": "Valor por defecto", "sql": "DEFAULT {value}", "unique": True},
            4: {"key": "check", "label": "Condición CHECK", "sql": "CHECK({check})", "unique": False},
        }
    }

    REAL_CHECKS = {
        1: {"label": "Mayor que", "sql": '"{col}" > {value}'},
        2: {"label": "Menor que", "sql": '"{col}" < {value}'},
        3: {"label": "Entre dos valores", "sql": '"{col}" BETWEEN {min} AND {max}'},
    }

    # --- Validar nombre ---
    while True:
        name = input("Digite el nombre de la columna: ")
        if is_valid_identifier(name):
            break
        print("⚠️ Nombre inválido. Use solo letras, números y _ (no puede iniciar con número).")

    column_parts = [name, REAL_MODEL["base"]]
    used_constraints = set()

    while True:
        print("\n--- Restricciones REAL disponibles ---")
        for num, data in REAL_MODEL["constraints"].items():
            status = ""
            if data["unique"] and data["key"] in used_constraints:
                status = " [Ya aplicado]"
            print(f"{num}. {data['label']}{status}")

        choice = input("Selecciona una opción (ENTER para finalizar): ")
        if not choice:
            break

        try:
            choice_idx = int(choice)
            constraint = REAL_MODEL["constraints"][choice_idx]
        except (ValueError, KeyError):
            print("⚠️ Opción no válida.")
            continue

        if constraint["unique"] and constraint["key"] in used_constraints:
            print("⚠️ Esta restricción ya fue agregada.")
            continue

        sql_piece = constraint["sql"]

        # DEFAULT
        if "{value}" in sql_piece and "{check}" not in sql_piece:
            while True:
                val = input("Valor por defecto (ej. 0.0): ")
                if is_valid_real(val):
                    break
                print("⚠️ Debe ser un número válido (ej: 10, -3, 4.5).")

            sql_piece = sql_piece.format(value=val)

        # CHECK
        elif "{check}" in sql_piece:
            print("\n--- Opciones de validación CHECK (REAL) ---")
            for num, data in REAL_CHECKS.items():
                print(f"{num}. {data['label']}")

            try:
                check_idx = int(input("Selecciona la opción de rango: "))
                check_template = REAL_CHECKS[check_idx]["sql"]
            except (ValueError, KeyError):
                print("⚠️ Opción inválida.")
                continue

            if "{value}" in check_template:
                while True:
                    val = input("Valor: ")
                    if is_valid_real(val):
                        break
                    print("⚠️ Debe ser un número válido.")

                check_sql = check_template.format(col=name, value=val)

            else:
                while True:
                    min_val = input("Valor mínimo: ")
                    max_val = input("Valor máximo: ")
                    if is_valid_real(min_val) and is_valid_real(max_val):
                        break
                    print("⚠️ Ambos valores deben ser números válidos.")

                check_sql = check_template.format(col=name, min=min_val, max=max_val)

            sql_piece = sql_piece.format(check=check_sql)

        column_parts.append(sql_piece)
        used_constraints.add(constraint["key"])

    final_sql = " ".join(column_parts)
    print(f"\n✅ Definición REAL generada: {final_sql}")

    return {"name": name, "sql": final_sql}


if __name__ == "__main__":
    resultado = generate_real_column_sql()
    print(f"Resultado: {resultado}")
