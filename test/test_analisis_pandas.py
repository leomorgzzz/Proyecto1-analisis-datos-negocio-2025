import os
from scripts.crear_base import crear_base
from scripts.insertar_datos import insertar_datos
from scripts.analisis_pandas import analisis_pandas
from config import TEST_DB_PATH, TEST_REPORT_PATH

def test_analisis_pandas():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    if os.path.exists(TEST_REPORT_PATH):
        os.remove(TEST_REPORT_PATH)

    crear_base(TEST_DB_PATH)
    insertar_datos(TEST_DB_PATH)

    analisis_pandas(TEST_DB_PATH, TEST_REPORT_PATH)

    assert os.path.exists(TEST_REPORT_PATH), "No se creó el reporte Excel."
