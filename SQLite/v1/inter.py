import re

def is_valid_identifier(name):
    """
    Valida que el nombre de columna sea válido en SQL.
    Debe comenzar con letra o _, y solo contener letras, números o _.
    """
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None


def is_valid_integer(value):
    """
    Valida que el valor sea un entero válido.
    """
    return re.match(r'^-?\d+$', value) is not None


def generate_integer_column_sql():
    """
    Genera la definición SQL de una columna INTEGER
    con validación de entradas.
    """

    INTEGER_MODEL = {
        "base": "INTEGER",
        "constraints": {
            1: {"key": "not_null", "label": "No permitir NULL", "sql": "NOT NULL", "unique": True},
            2: {"key": "unique", "label": "Valor único", "sql": "UNIQUE", "unique": True},
            3: {"key": "default", "label": "Valor por defecto", "sql": "DEFAULT {value}", "unique": True},
            4: {"key": "check", "label": "Condición CHECK", "sql": "CHECK({check})", "unique": False},
        }
    }

    INTEGER_CHECKS = {
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

    column_parts = [name, INTEGER_MODEL["base"]]
    used_constraints = set()

    while True:
        print("\n--- Restricciones INTEGER disponibles ---")
        for num, data in INTEGER_MODEL["constraints"].items():
            status = ""
            if data["unique"] and data["key"] in used_constraints:
                status = " [Ya aplicado]"
            print(f"{num}. {data['label']}{status}")

        choice = input("Selecciona una opción (ENTER para finalizar): ")
        if not choice:
            break

        try:
            choice_idx = int(choice)
            constraint = INTEGER_MODEL["constraints"][choice_idx]
        except (ValueError, KeyError):
            print("⚠️ Opción no válida.")
            continue

        if constraint["unique"] and constraint["key"] in used_constraints:
            print("⚠️ Esta restricción ya fue agregada.")
            continue

        sql_piece = constraint["sql"]

        # DEFAULT
        if "{value}" in sql_piece:
            while True:
                val = input("Valor por defecto (entero): ")
                if is_valid_integer(val):
                    break
                print("⚠️ Debe ser un número entero válido.")
            sql_piece = sql_piece.format(value=val)

        # CHECK
        elif "{check}" in sql_piece:
            print("\n--- Opciones de validación CHECK ---")
            for num, data in INTEGER_CHECKS.items():
                print(f"{num}. {data['label']}")

            try:
                check_idx = int(input("Selecciona la opción: "))
                check_template = INTEGER_CHECKS[check_idx]["sql"]
            except (ValueError, KeyError):
                print("⚠️ Opción inválida.")
                continue

            if "{value}" in check_template:
                while True:
                    val = input("Valor entero: ")
                    if is_valid_integer(val):
                        break
                    print("⚠️ Debe ser un número entero válido.")
                check_sql = check_template.format(col=name, value=val)
            else:
                while True:
                    min_val = input("Valor mínimo: ")
                    max_val = input("Valor máximo: ")
                    if is_valid_integer(min_val) and is_valid_integer(max_val):
                        break
                    print("⚠️ Ambos valores deben ser enteros válidos.")
                check_sql = check_template.format(col=name, min=min_val, max=max_val)

            sql_piece = sql_piece.format(check=check_sql)

        column_parts.append(sql_piece)
        used_constraints.add(constraint["key"])

    final_sql = " ".join(column_parts)
    print(f"\n✅ Definición generada: {final_sql}")
    
    # 🔥 CAMBIO AQUÍ: Ahora devolvemos un diccionario con el nombre y el SQL
    # Esto hace que 'xxx.py' funcione sin errores y que PK/FK encuentren la columna
    return {"name": name, "sql": final_sql}


if __name__ == "__main__":
    resultado = generate_integer_column_sql()
    print(f"Resultado para el orquestador: {resultado}")