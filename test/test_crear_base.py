import os
from scripts.crear_base import crear_base
from config import TEST_DB_PATH

def test_crear_base():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    crear_base(TEST_DB_PATH)

    assert os.path.exists(TEST_DB_PATH), "No se creó la base de datos."
