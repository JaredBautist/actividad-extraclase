# Create a downloadable README.md file with the requested content
readme_content = """# Entrega — Actividades de Testing (Pág. 13, 14 y 15)

Este repositorio contiene tres actividades prácticas de **Técnicas de Testing de Software**:

y estos son los comandos para ejecutar cada una de ellas

**Actividad Página 13**
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=%CD%
pytest -v

**Actividad Página 14**
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=%CD%
pytest -q --cov=src --cov-branch --cov-config=.coveragerc --cov-report=term-missing --cov-report=html
start htmlcov\index.html

**Actividad Página 15**
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=%CD%
pytest
