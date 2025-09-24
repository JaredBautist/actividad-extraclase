import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_remove_updates_internal_state_consistently():
    todo = ToDo()
    a = todo.add('A'); b = todo.add('B'); c = todo.add('C')
    assert len(todo.list()) == 3
    assert todo.remove(b.id) is True
    ids = [t.id for t in todo.list()]
    assert ids == [a.id, c.id]

def test_many_items_have_unique_ids_and_filtering_is_stable():
    todo = ToDo()
    N = 1000
    for i in range(N):
        todo.add(f'T{i}', priority=('high' if i % 2 == 0 else 'low'))
    assert todo.next_id() == N + 1
    highs = todo.list(priority='high'); lows = todo.list(priority='low')
    assert len(highs) + len(lows) == N
    assert all(t.priority in ('high', 'low') for t in highs + lows)
