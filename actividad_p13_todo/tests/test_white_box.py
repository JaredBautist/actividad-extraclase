import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_toggle_done_true_then_true_again():
    todo = ToDo()
    t = todo.add('A')
    assert todo.toggle_done(t.id) is True
    assert todo.get(t.id).done is True
    assert todo.toggle_done(t.id) is True
    assert todo.get(t.id).done is False

def test_toggle_done_returns_false_when_not_found():
    todo = ToDo()
    assert todo.toggle_done(12345) is False

def test_loop_states_0_1_N_elements():
    todo = ToDo()
    assert len(todo) == 0
    todo.add('A')
    assert len(todo) == 1
    for i in range(10):
        todo.add(f'T{i}')
    assert len(todo) == 11

def test_update_paths_and_validations():
    todo = ToDo()
    t = todo.add('A', priority='medium', description=None)
    assert todo.update(t.id, title='B', priority='high', description='x') is True
    updated = todo.get(t.id)
    assert (updated.title, updated.priority, updated.description) == ('B', 'high', 'x')
    assert todo.update(999, title='C') is False
    with pytest.raises(ValueError):
        todo.update(t.id, title='   ')
