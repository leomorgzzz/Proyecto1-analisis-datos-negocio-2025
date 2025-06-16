import sqlite3
import pandas as pd

conn = sqlite3.connect('empresa.db')

clientes = pd.read_sql_query("SELECT * FROM Clientes", conn)
productos = pd.read_sql_query("SELECT * FROM Productos", conn)
ventas = pd.read_sql_query("SELECT * FROM Ventas", conn)

conn.close()

ventas_full = ventas.merge(clientes, on='id_cliente').merge(productos, on='id_producto')

ventas_full['total_venta'] = ventas_full['cantidad'] * ventas_full['precio']

ventas_totales = ventas_full['total_venta'].sum()
print(f"Ventas totales generadas: ${ventas_totales:.2f}")

productos_unidades = ventas_full.groupby('nombre_producto')['cantidad'].sum().sort_values(ascending=False)
print("\nProductos más vendidos (unidades):")
print(productos_unidades)

clientes_top = ventas_full.groupby('nombre_cliente')['total_venta'].sum().sort_values(ascending=False)
print("\nClientes que más compraron:")
print(clientes_top)

ventas_region = ventas_full.groupby('ubicacion')['total_venta'].sum().sort_values(ascending=False)
print("\nVentas por región:")
print(ventas_region)

ventas_full['fecha'] = pd.to_datetime(ventas_full['fecha'])
ventas_full['mes'] = ventas_full['fecha'].dt.to_period('M')
ventas_mes = ventas_full.groupby('mes')['total_venta'].sum()

print("\nVentas por mes:")
print(ventas_mes)

with pd.ExcelWriter("reporte_analisis.xlsx") as writer:
    ventas_full.to_excel(writer, sheet_name="Ventas Detalle", index=False)
    productos_unidades.to_frame("Unidades Vendidas").to_excel(writer, sheet_name="Productos Unidades")
    clientes_top.to_frame("Total Comprado").to_excel(writer, sheet_name="Clientes Top")
    ventas_region.to_frame("Ventas por Región").to_excel(writer, sheet_name="Ventas Región")
    ventas_mes.to_frame("Ventas por Mes").to_excel(writer, sheet_name="Ventas Mes")

print("\nReporte exportado a reporte_analisis.xlsx")
