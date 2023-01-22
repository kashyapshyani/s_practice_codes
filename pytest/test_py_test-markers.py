import pytest

@pytest.mark.login
def test_m4():
    a=5
    b=4
    assert a-1==b , "test passed"
    assert a==b+1 , "test failed"
    
# @pytest.mark.login   
def test_m5():
    name = "selenium"
    assert name.upper() == "SELENIuM"

@pytest.mark.login
def test_m6():
    assert False

#run wirh command - py.test -m login -v
    