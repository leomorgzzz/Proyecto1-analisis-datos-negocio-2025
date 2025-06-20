import sqlite3
import os

def crear_base(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    print(f"Creando/Conectando base de datos en: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cliente TEXT NOT NULL,
        ubicacion TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_producto INTEGER,
        fecha TEXT,
        cantidad INTEGER,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
        FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
    )
    ''')

    conn.commit()
    conn.close()

    print("Base de datos y tablas creadas con éxito.")

if __name__ == "__main__":
    db_path = os.path.join("data", "sample", "empresa.db")
    crear_base(db_path)
