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


def test_part2_2_letter():
    entry = "two1nine"
    assert day_one.get_digits(entry) == "29"


def test_part2_3_letter():
    entry = "eightwothree"
    assert day_one.get_digits(entry) == "83"


def test_part2_digit_letter():
    entry = "abcone2threexyz"
    assert day_one.get_digits(entry) == "13"


def test_part2_digit_letter2():
    entry = "xtwone3four"
    assert day_one.get_digits(entry) == "24"


def test_part2_digit():
    entry = "4nineeightseven2"
    assert day_one.get_digits(entry) == "42"


def test_part2_letters_many_digit():
    entry = "zoneight234"
    assert day_one.get_digits(entry) == "14"


def test_part2_digit_sixteen():
    entry = "7pqrstsixteen"
    assert day_one.get_digits(entry) == "76"


def test_use_1():
    entry = "ghthreetwo1mhgtklfqdkqthree7seventwone"
    assert day_one.get_digits(entry) == "31"


def test_use_2():
    entry = "ghthreetwo1mhgtklfqdkqthree7seventwonethree"
    assert day_one.get_digits(entry) == "33"


def test_one_letter():
    entry = "one"
    assert day_one.get_digits(entry) == "11"


def test_use_3():
    entry = "oneoneoneone2"
    assert day_one.get_digits(entry) == "12"


def test_use_4():
    entry = "nineghthreetwo1mhgtklfqdkqthree7seventwone"
    assert day_one.get_digits(entry) == "91"


def test_use_5():
    entry = "s8twoned"
    assert day_one.get_digits(entry) == "81"


def test_use_6():
    entry = "stwoned8"
    assert day_one.get_digits(entry) == "28"
