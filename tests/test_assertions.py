def test_equals():
    assert 1 == 1

def test_greater():
    assert 2 > 1

def test_less_than():
    assert 1 < 2

def test_not_equal():
    assert 1 != 2

def test_greater_or_equal():
    assert 2 >= 2

def test_less_or_equal():
    assert 1 <= 2

def test_tuple_equals_tuple():
    assert (1,2) == (1,2)

def test_element_exists_in_list():
    assert 2 in [1,2]

def test_string_equals_strin():
    assert "abc" == "abc"