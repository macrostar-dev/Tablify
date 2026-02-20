from blob import generate_blob_column_sql
from inter import generate_integer_column_sql
from real import generate_real_column_sql
from text import generate_text_column_sql
from pk import add_primary_keys
from foreign_key import add_foreign_keys

column_options = {
    1: {"name": "INTEGER", "function": generate_integer_column_sql},
    2: {"name": "TEXT", "function": generate_text_column_sql},
    3: {"name": "BLOB", "function": generate_blob_column_sql},
    4: {"name": "REAL", "function": generate_real_column_sql},
    5: {"name": "PRIMARY_KEY", "function": add_primary_keys},
    6: {"name": "FOREIGN_KEY", "function": add_foreign_keys},
}

table_name = input("Digite el nombre de la tabla: ")

columns = []

while True:
    print("\nSeleccione el tipo de columna (Enter para terminar):")
    
    for num, data in column_options.items():
        print(f"{num}. {data['name']}")

    option_input = input("Opción: ")

    if option_input == "":
        break

    if not option_input.isdigit():
        print("⚠️ Opción inválida.")
        continue

    option_selection = int(option_input)

    if option_selection not in column_options:
        print("⚠️ Opción no existe.")
        continue

    if option_selection in [5, 6]:
        column_options[option_selection]["function"](columns)
        continue

    result_dict = column_options[option_selection]["function"]()

    if not isinstance(result_dict, dict) or "name" not in result_dict or "sql" not in result_dict:
        print("⚠️ Error: la función no retornó el formato esperado.")
        continue

    columns.append(result_dict)

if not columns:
    print("\n❌ No se agregaron columnas. No se pudo generar la tabla.")
else:
    body = ",\n    ".join(col["sql"] for col in columns)
    sql_command = f"CREATE TABLE {table_name} (\n    {body}\n);"

    print("\n" + "="*30)
    print("🚀 SENTENCIA SQL GENERADA:")
    print("="*30)
    print(sql_command)

