import pytest
from  test_sq import square

def test_postive():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0
def test_string():
    with pytest.raises(TypeError):
        square("Dog")