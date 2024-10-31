from ..calculator import addition
from pytest import raises, mark

#tests for travis
# test new credits

# testing functionality of addition
def test_addition():

    result = addition(2,3)
    assert result ==5 

# test wrong input
def test_addition_input():

    with raises(ValueError, match ='Input must be an integer or float'):
        addition('s', 3)