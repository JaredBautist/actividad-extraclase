import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_user_journey_smoke():
    t = ToDo()
    t.add('Comprar pan', priority='high')
    t.add('Hacer gym', priority='low')
    assert len(t.list()) == 2
    assert t.toggle_done(1) is True
    assert [x.title for x in t.list(done=True)] == ['Comprar pan']
