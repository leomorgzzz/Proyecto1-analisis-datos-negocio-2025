import sqlite3
import pandas as pd
import os

def analisis_pandas(db_path, output_report_path):
    os.makedirs(os.path.dirname(output_report_path), exist_ok=True)

    conn = sqlite3.connect(db_path)

    df_clientes = pd.read_sql_query("SELECT * FROM Clientes", conn)
    df_productos = pd.read_sql_query("SELECT * FROM Productos", conn)
    df_ventas = pd.read_sql_query("SELECT * FROM Ventas", conn)

    conn.close()

    print("Clientes: ")
    print(df_clientes.head())
    print("\nProductos: ")
    print(df_productos.head())
    print("\nVentas: ")
    print(df_ventas.head())

    with pd.ExcelWriter(output_report_path) as writer:
        df_clientes.to_excel(writer, sheet_name="Clientes", index=False)
        df_productos.to_excel(writer, sheet_name="Productos", index=False)
        df_ventas.to_excel(writer, sheet_name="Ventas", index=False)

    print(f"\nDatos exportados a {output_report_path}")

if __name__ == "__main__":
    analisis_pandas("data/sample/empresa.db", "reports/reporte_analisis.xlsx")
