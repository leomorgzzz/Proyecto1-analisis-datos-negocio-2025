# Proyecto 1 — Análisis de Ventas de Negocio (End-to-End)

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

📦 Proyecto1-analisis-datos-negocio

- ── crear_base.py ------------> # Creación de la base de datos y tablas
- ── insertar_datos.py --------> # Inserción de datos simulados
- ── consultas_sql.py ---------> # Consultas básicas de ejemplo
- ── analisis_avanzado.py -----> # Análisis completo de ventas
- ── graficos.py --------------> # Visualización automatizada de resultados
- ── empresa.db ---------------> # Base de datos SQLite generada
- ── reporte_analisis.xlsx ----> # Reporte final en Excel
- ── grafico_region.png -------> # Gráfico de ventas por región
- ── grafico_mes.png ----------> # Gráfico de ventas por mes
- ── grafico_productos.png ----> # Gráfico de top productos
- ── README.md ----------------> # Descripción del proyecto

---

## 📈 Ejemplos de resultados

## Ventas por Región
![Ventas por región](grafico_region.png)

## Ventas por Mes
![Ventas por región](grafico_mes.png)

## Producto más vendido
![Ventas por región](grafico_productos.png)

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar este repositorio:

```bash
git clone https://github.com/leomorgzzz/Proyecto1-analisis-datos-negocio
cd Proyecto1-analisis-datos-negocio
```
2. (Opcional) Crear un entorno virtual en Anaconda o venv.

3. Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```
4. Ejecutar el pipeline completo:

```bash
python ejecutar_todo.py
```
5. (Opcional) Puede ejecutar cualquier otro archivo .py independientemente siguiendo la misma estructura. Ejemplo:

```bash
python consultas_sql.py
```

6. Listo! Ya puede visualizar los archivos de Excel (.xlsx) y las Gráficas en formato PNG.