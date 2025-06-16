import subprocess

scripts = [
    "crear_base.py",
    "insertar_datos.py",
    "consultas_sql.py",
    "analisis_avanzado.py",
    "graficos.py"
]

for script in scripts:
    print(f"\nEjecutando {script}...")
    resultado = subprocess.run(["python", script])
    if resultado.returncode != 0:
        print(f"Error al ejecutar {script}. Deteniendo ejecución.")
        break

print("\nProceso completo.")
