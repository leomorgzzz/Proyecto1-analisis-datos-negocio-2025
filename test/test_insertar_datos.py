import os
from scripts.crear_base import crear_base
from scripts.insertar_datos import insertar_datos
from config import TEST_DB_PATH

def test_insertar_datos():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    crear_base(TEST_DB_PATH)
    insertar_datos(TEST_DB_PATH)

   
