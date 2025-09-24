import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_add_and_get():
    from src.todo import ToDo
    t = ToDo()
    a = t.add('A', priority='high')
    assert t.get(a.id) is not None
    assert a.title == 'A' and a.priority == 'high'
def test_update_validation_and_paths():
    from src.todo import ToDo
    t = ToDo()
    a = t.add('A')
    assert t.update(a.id, title='B', priority='low', description='x', done=True)
    b = t.get(a.id)
    assert (b.title, b.priority, b.description, b.done) == ('B','low','x',True)
