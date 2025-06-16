# Proyecto 1 — Análisis de Ventas de Negocio (End-to-End)
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.10+-blue)

Este proyecto fue desarrollado como parte de mi formación en Ciencias Genómicas. Aunque mi campo es la bioinformática, aquí aplico herramientas de análisis de datos enfocadas a contextos empresariales, desarrollando habilidades que son transferibles tanto a la industria como a la investigación.

Este proyecto simula un caso real de análisis de ventas para un negocio utilizando un flujo de trabajo profesional de ciencia de datos. Incluye desde la creación de bases de datos SQL, consultas, análisis en Python, visualización de datos y exportación de reportes automatizados.

---

## 🔧 Tecnologías utilizadas

- Python 3.12
- SQLite
- pandas
- matplotlib
- seaborn
- Excel (openpyxl)
- Git & GitHub
- VSCode + Anaconda

---

## 📊 Objetivo del proyecto

El objetivo es demostrar dominio de herramientas fundamentales de análisis de datos realizando:

- Creación de base de datos relacional.
- Ingesta y limpieza de datos.
- Análisis descriptivo de ventas, clientes y productos.
- Generación de KPIs clave.
- Visualización de resultados.
- Exportación automatizada de reportes en Excel.


---

## 📁 Estructura de archivos
```bash
📦 Proyecto1-analisis-datos-negocio-2025
├── data
│   └── sample
│       └── empresa.db             # Base de datos SQLite generada y usada
├── reports
│   └── reporte_analisis.xlsx      # Reporte final en Excel con análisis
├── figures
│   ├── grafico_region.png         # Gráfico de ventas por región
│   ├── grafico_mes.png            # Gráfico de ventas por mes
│   └── grafico_productos.png      # Gráfico de top productos
├── scripts
│   ├── crear_base.py              # Creación de la base de datos y tablas
│   ├── insertar_datos.py          # Inserción de datos simulados
│   ├── consultas_sql.py           # Consultas básicas de ejemplo
│   ├── analisis_avanzado.py       # Análisis completo de ventas
│   ├── graficos.py                # Visualización automatizada de resultados
│   └── ejecutar_todo.py           # Script para correr todo en orden
├── .gitignore                     # Archivos y carpetas ignoradas por git
├── LICENSE                        # Licencia del proyecto
├── README.md                      # Documentación y descripción del proyecto
├── requirements.txt               # Dependencias del proyecto
└── AUTHORS.md                     # Autores y colaboradores

```
---

## 📈 Ejemplos de resultados

## Ventas por Región
![Ventas por región](figures/grafico_region.png)

## Ventas por Mes
![Ventas por región](figures/grafico_mes.png)

## Producto más vendido
![Ventas por región](figures/grafico_productos.png)

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar este repositorio:

```bash
git clone https://github.com/leomorgzzz/Proyecto1-analisis-datos-negocio
cd Proyecto1-analisis-datos-negocio
```
2. (Opcional) Crear un entorno virtual en Anaconda o venv.
```bash
conda create -n proyecto1 python=3.11
conda activate proyecto1
pip install -r requirements.txt
```

3. Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```
4. Ejecutar el pipeline completo:

```bash
python scripts/ejecutar_todo.py

```
5. (Opcional) Puede ejecutar cualquier otro archivo .py independientemente siguiendo la misma estructura. Ejemplo:

```bash
python scripts/consultas_sql.py
```

6. Listo! Ya puede visualizar los archivos de Excel (.xlsx) y las Gráficas en formato PNG.

---

## 👤 Autor

Creado por **Leonardo Morales Rodríguez (leomorgzzz)** 