# Ensure project root and src/ are importable on Windows/Py 3.13
import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC  = os.path.join(ROOT, 'src')
for p in (ROOT, SRC):
    if p not in sys.path:
        sys.path.insert(0, p)

import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo
@pytest.fixture
def todo():
    return ToDo()
@pytest.fixture
def ten_tasks(todo):
    for i in range(10):
        todo.add(f'T{i}', priority=('high' if i%2==0 else 'low'))
    return todo
