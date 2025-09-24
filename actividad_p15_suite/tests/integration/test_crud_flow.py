import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_full_flow(ten_tasks):
    todo = ten_tasks
    count = len(todo)
    ids = [t.id for t in todo.list()[:3]]
    for i in ids:
        assert todo.toggle_done(i)
    assert todo.remove(ids[0]) is True
    assert len(todo) == count - 1
    dones = todo.list(done=True)
    assert all(d.done for d in dones)
    highs = todo.list(priority='high'); lows = todo.list(priority='low')
    assert len(highs)+len(lows) == len(todo)
