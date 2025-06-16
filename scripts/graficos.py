import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set(style='whitegrid', palette='muted', font_scale=1.5)

conn = sqlite3.connect('empresa.db')

clientes = pd.read_sql_query("SELECT * FROM Clientes", conn)
productos = pd.read_sql_query("SELECT * FROM Productos", conn)
ventas = pd.read_sql_query("SELECT * FROM Ventas", conn)

conn.close()

ventas_full = ventas.merge(clientes, on='id_cliente').merge(productos, on='id_producto')
ventas_full['total_venta'] = ventas_full['cantidad'] * ventas_full['precio']
ventas_full['fecha'] = pd.to_datetime(ventas_full['fecha'])
ventas_full['mes'] = ventas_full['fecha'].dt.to_period('M')

ventas_region = ventas_full.groupby('ubicacion')['total_venta'].sum().sort_values(ascending=False)
plt.figure(figsize=(9, 6))
sns.barplot(x=ventas_region.index, y=ventas_region.values)
plt.title("Ventas dependiendo de la Región")
plt.ylabel("Total de Ventas")
plt.xlabel("Región")
plt.tight_layout()
plt.savefig("grafico_region.png")
plt.close()

ventas_mes = ventas_full.groupby('mes')['total_venta'].sum()
plt.figure(figsize=(10, 6))
ventas_mes.plot(marker='o')
plt.title("Ventas por Mes")
plt.ylabel("Total de Ventas")
plt.xlabel("Mes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_mes.png")
plt.close()

productos_unidades = ventas_full.groupby('nombre_producto')['cantidad'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(9, 6))
sns.barplot(x=productos_unidades.values, y=productos_unidades.index)
plt.title("5 Productos más Unidades Vendidas")
plt.xlabel("Unidades Vendidas")
plt.ylabel("Producto")
plt.tight_layout()
plt.savefig("grafico_productos.png")
plt.close()

print("Gráficos generados y guardados en archivos .png")
