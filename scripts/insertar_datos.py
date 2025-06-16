import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

Clientes = [
    ("Refaccionaria Yaquison", "Norte"),
    ("Distribuidora Nari", "Sur"),
    ("Comercial BAT", "Este"),
    ("Servicios MarKa", "Oeste"),
    ("Proveedor Namos", "Centro")
]

Productos = [
    ("RT-600041","Baleros", 1800),
    ("Impresora", "Tecnología", 3500),
    ("Escritorio", "Muebles", 4500),
    ("Laptop", "Tecnología", 15000),
    ("Monitor", "Tecnología", 7000)
]

cursor.executemany("INSERT INTO Clientes (nombre_cliente, ubicacion) VALUES (?, ?)", Clientes)

cursor.executemany("INSERT INTO Productos (nombre_producto, categoria, precio) VALUES (?, ?, ?)", Productos)

for _ in range(20):
    id_cliente = random.randint(1, 5)
    id_producto = random.randint(1, 5)
    fecha = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    cantidad = random.randint(1,10)
    cursor.execute(
        "INSERT INTO Ventas (id_cliente, id_producto, fecha, cantidad) VALUES (?, ?, ?, ?)",
        (id_cliente, id_producto, fecha, cantidad)
    )
conn.commit()
conn.close()

print("Los datos fueron insertados con éxito.")