def get_initial_hit_points(player_class: str) -> int:
    pass




class PlayerClass(Enum):
    WARRIOR = 1
    KNIGHT = 2
    SORCERER = 3
    CLERIC = 4

import warnings

def get_initial_hit_points(player_class: Union[PlayerClass, str]) -> int:
    if isinstance(player_class, str):
        msg = 'Using player_class as str has been deprecated' \
        'and will be removed in the future'
        warnings.warn(DeprecationWarning(msg))
        player_class = get_player_enum_from_string(player_class)
        # ..

def test_get_initial_hit_points_warning():
    with pytest.warns(DeprecationWarning,
                        match='.*str has been deprecated.*'):
        get_initial_hit_points('warrior')



def test_simple_math():
    assert abs(0.1 + 0.2) - 0.3 < 0.0001


def test_approx_simple():
    assert 0.1 + 0.2 == approx(0.3)


def test_approx_list():
    assert [0.1 + 1.2, 0.2 + 0.8] == approx([1.3, 1.0])


def test_approx_dict():
    values = {'v1': 0.1 + 1.2, 'v2': 0.2 + 0.8}
    assert values == approx(dict(v1=1.3, v2=1.0))


def test_approx_numpy():
    import numpy as np
    values = np.array([0.1, 0.2]) + np.array([1.2, 0.8])
    assert values == approx(np.array([1.3, 1.0]))


import hashlib

def commit_hash(contents):
    size = len(contents)
    print('content size', size)
    hash_contents = str(size) + '\0' + contents
    result = hashlib.sha1(hash_contents.encode('UTF-8')).hexdigest()
    print(result)
    return result[:8]

def test_commit_hash():
    contents = 'some text contents for commit'
    assert commit_hash(contents) == '0cf85793'




