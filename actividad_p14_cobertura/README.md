# Actividad Página 14 — Medición de Cobertura
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=%CD%
pytest -q --cov=src --cov-branch --cov-config=.coveragerc --cov-report=term-missing --cov-report=html
start htmlcov\index.html
```
