import sqlite3
import pandas as pd 

conn = sqlite3.connect('empresa.db')

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

with pd.ExcelWriter("reporte_inicial.xlsx") as writer:
    df_clientes.to_excel(writer, sheet_name="Clientes", index=False)
    df_productos.to_excel(writer, sheet_name="Productos", index=False)
    df_ventas.to_excel(writer, sheet_name="Ventas", index=False)

print("\nDatos exportados a reporte_inicial.xlsx")