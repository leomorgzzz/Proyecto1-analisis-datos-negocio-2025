import sqlite3
from config import DB_PATH

def insertar_datos(db_path="data/sample/empresa.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    Clientes = [
        ("Refaccionaria Yaquison", "Norte"),
        ("Distribuidora Nari", "Sur"),
        ("Servicios MarKa", "Oeste"),
        ("Proveedor Namos", "Centro"),
        ("Comercial BAT", "Este")
    ]

    Productos = [
        ("Laptop", "Electrónica", 15000),
        ("Impresora", "Electrónica", 3000),
        ("Escritorio", "Muebles", 5000),
        ("Monitor", "Electrónica", 4000),
        ("RT-600041", "Componentes", 2000)
    ]

    cursor.executemany("INSERT INTO Clientes (nombre_cliente, ubicacion) VALUES (?, ?)", Clientes)
    cursor.executemany("INSERT INTO Productos (nombre_producto, categoria, precio) VALUES (?, ?, ?)", Productos)

    conn.commit()
    conn.close()

    print("Los datos fueron insertados con éxito.")


