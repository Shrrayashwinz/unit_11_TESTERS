"""
test_Lab11_pcarswel-1.py
Author: Shrrayash
Purpose: Test normalize_rotation function from Lab11_pcarswel-1.py using pytest.
Date: November 3, 2025
"""

from py_test import normalize_rotation
import pytest

def test_rotation_100():
    assert normalize_rotation(100) == 100

def test_rotation_460():
    assert normalize_rotation(460) == 100

def test_rotation_820():
    assert normalize_rotation(820) == 100

def test_rotation_negative_100():
    assert normalize_rotation(-100) == 260

def test_rotation_negative_460():
    assert normalize_rotation(-460) == 260

def test_rotation_negative_820():
    assert normalize_rotation(-820) == 260

def test_rotation_non_numeric():
    with pytest.raises(ValueError):
        normalize_rotation("not a number")
