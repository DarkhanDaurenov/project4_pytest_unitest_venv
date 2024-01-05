from utils import dicts

def test_get_val():
    assert dicts.get_val({'one':'one','two':'two','three':'three'}, key='one', default='git') == 'one'
    assert dicts.get_val({'one': 'one', 'two': 'two', 'three': 'three'}, key='two', default='git') == 'two'
    assert dicts.get_val({'one': 'one', 'two': 'two', 'three': 'three'}, key=None, default='git') == 'git'
