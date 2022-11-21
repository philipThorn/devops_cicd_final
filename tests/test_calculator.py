from shop_app.calculator import Calculator

def test_class():
    calc = Calculator(1,2)
    assert calc


def test_add():
    calc = Calculator(1,2)
    assert calc.add() == 3

def test_multiply():
    calc = Calculator(2,2)
    assert calc.multiply() == 4

