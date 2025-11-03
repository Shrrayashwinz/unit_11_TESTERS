import pytest
from example_code import divide, is_even


def test_divide_with_correct_input():
    assert divide (40, 5) == 8
    assert divide (78, 13) == 6
    assert divide (285, 19) == 15
    assert divide (69, 3) == 23
    assert divide (4700000, 10) == 470000

def test_divide_by_zero_input():
    assert divide (10, 0) == None


def test_is_even_correct_inputs():
    for i in range(1, 100):
        if i % 2 == 0:
            assert is_even(i) == True
        else:
            assert is_even(i) == False

    assert is_even(5) == False 

def test_divide_using_string():
    assert divide ('10', 2) == None
     