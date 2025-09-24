# 🧪 Entrega — Actividades de Testing (Pág. 13, 14 y 15)



## 🔧 Requisitos
- **Python 3.10+**
- **pip** y **venv** instalados
- Conexión para instalar dependencias (`pytest`, `pytest-cov`)

> ⚠️ Ejecuta cada bloque **dentro de la carpeta** de su actividad:
> - `actividad_p13_todo/`
> - `actividad_p14_cobertura/`
> - `actividad_p15_suite/`

---

## ✨ Actividad Página 13 

- python -m venv .venv
-.venv\Scripts\activate
- pip install -r requirements.txt
- set PYTHONPATH=%CD%
- pytest -v

## ✨ Actividad Página 14

- python -m venv .venv
- .venv\Scripts\activate
- pip install -r requirements.txt
- set PYTHONPATH=%CD%
- pytest -q --cov=src --cov-branch --cov-config=.coveragerc --cov-report=term-missing --cov-report=html
- start htmlcov\index.html

## ✨ Actividad Página 15
- python -m venv .venv
- .venv\Scripts\activate
- pip install -r requirements.txt
- set PYTHONPATH=%CD%
- pytest
