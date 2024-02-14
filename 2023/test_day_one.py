import pytest 

import day_one

def test_first_last():
    entry = "1abc2"
    assert day_one.get_digits(entry) == "12"
    
def test_inside():
    entry = "pqr3stu8vwx"
    assert day_one.get_digits(entry) == "38"

def test_many():
    entry = "a1b2c3d4e5f"
    assert day_one.get_digits(entry) == "15"

def test_one():
    entry = "treb7uchet"
    assert day_one.get_digits(entry) == "77"