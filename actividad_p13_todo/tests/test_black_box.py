import pytest
try:
    from src.todo import ToDo
except ModuleNotFoundError:
    from todo import ToDo

def test_add_requires_title():
    todo = ToDo()
    with pytest.raises(ValueError):
        todo.add('   ')

def test_priority_domain_only_valid_values():
    todo = ToDo()
    with pytest.raises(ValueError):
        todo.add('Task', priority='urgent')

def test_add_trims_title_and_returns_task():
    todo = ToDo()
    t = todo.add('  Comprar leche  ', priority='high')
    assert t.title == 'Comprar leche'
    assert t.priority == 'high'
    assert t.done is False

def test_list_empty_returns_empty():
    assert ToDo().list() == []

def test_remove_non_existing_returns_false():
    todo = ToDo(); todo.add('A')
    assert todo.remove(9999) is False

def test_list_filters_by_priority_and_done():
    todo = ToDo()
    a = todo.add('A', priority='low')
    b = todo.add('B', priority='high')
    todo.toggle_done(b.id)
    lows = todo.list(priority='low')
    dones = todo.list(done=True)
    assert [t.id for t in lows] == [a.id]
    assert [t.id for t in dones] == [b.id]
