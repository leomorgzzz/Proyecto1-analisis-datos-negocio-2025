import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "sample", "empresa.db")
REPORT_PATH = os.path.join(BASE_DIR, "reports", "reporte_analisis.xlsx")

TEST_DIR = os.path.join(BASE_DIR, "test")
TEST_DB_PATH = os.path.join(TEST_DIR, "test_empresa.db")
TEST_REPORT_PATH = os.path.join(TEST_DIR, "test_reporte.xlsx")
