import pytest

@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run1(order=1)
def test_foo1():
    assert True

@pytest.mark.run2(order=0)
def test_foo2():
    assert True    

@pytest.mark.loa(order=2)
def test_lo1():
    assert True        