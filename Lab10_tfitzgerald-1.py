"""
Lab 10
rotation
Tyson Fitzgerald
7/11/2025

"""
import pytest

def change_rotation(degrees):

    try:
        return int(degrees) % 360
    except (ValueError):
        raise ValueError("Input has to be a number")

def test_a():
    assert change_rotation(100) == 100

def test_b():
    assert change_rotation(460) == 100

def test_c():
    assert change_rotation(820) == 100

def test_d():
    assert change_rotation(-100) == 260

def test_e():
    assert change_rotation(-460) == 260

def test_f():
    assert change_rotation(-820) == 260

def test_g():
    with pytest.raises(ValueError):
        change_rotation("non number")