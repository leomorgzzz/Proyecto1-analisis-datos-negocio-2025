import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Ventas")
total_ventas = cursor.fetchone()[0]
print(f"\nTotal de ventas registradas: {total_ventas}")


cursor.execute("SELECT SUM(cantidad) FROM Ventas")
total_productos = cursor.fetchone()[0]
print(f"\nTotal de productos vendidos: {total_productos}")

cursor.execute('''
    SELECT Productos.nombre_producto, SUM(Ventas.cantidad) AS total_vendido
    FROM Ventas
    JOIN Productos ON Ventas.id_producto = Productos.id_producto
    GROUP BY Productos.nombre_producto
    ORDER BY total_vendido DESC
    LIMIT 1
''')

producto_maximo = cursor.fetchone()
print(f"\nProducto más vendido: {producto_maximo[0]} con {producto_maximo[1]} unidades")

cursor.execute('''
    SELECT Clientes.nombre_cliente, SUM(Ventas.cantidad) AS total_comprado
    FROM Ventas
    JOIN Clientes ON Ventas.id_cliente = Clientes.id_cliente
    GROUP BY Clientes.nombre_cliente
    ORDER BY total_comprado DESC
''')

clientes = cursor.fetchall()
print("\nClientes por volumen de compra: ")
for cliente in clientes:
    print(f"{cliente[0]} compró {cliente[1]} unidades")

cursor.execute('''
    SELECT Clientes.ubicacion, SUM(Ventas.cantidad) AS total_por_region
    FROM Ventas
    JOIN Clientes ON Ventas.id_cliente = Clientes.id_cliente
    GROUP BY Clientes.ubicacion
''')

zonas = cursor.fetchall()
for zona in zonas:
    print(f"{zona[0]}: {zona[1]} unidades")

conn.close()