import subprocess

scripts = [
    "scripts/crear_base.py",
    "scripts/insertar_datos.py",
    "scripts/consultas_sql.py",
    "scripts/analisis_pandas.py",
    "scripts/analisis_avanzado.py",
    "scripts/graficos.py"
]

for script in scripts:
    print(f"\nEjecutando {script}...")
    resultado = subprocess.run(["python", script])
    if resultado.returncode != 0:
        print(f"Error al ejecutar {script}. Deteniendo ejecución.")
        break

print("\nProceso completo.")
