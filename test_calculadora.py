import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_suma(calc):
    assert calc.suma(2, 3) == 5
    assert calc.suma(-1, 1) == 0
    assert calc.suma(2.5, 0.5) == 3.0

def test_resta(calc):
    assert calc.resta(5, 2) == 3
    assert calc.resta(-1, -1) == 0
    assert calc.resta(2.5, 1.25) == 1.25

def test_divide_normal(calc):
    assert calc.divide(10, 2) == 5
    assert pytest.approx(calc.divide(5, 2), 0.0001) == 2.5

def test_divide_por_cero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)

if __name__ == "__main__":
    pytest.main(["-q"])
