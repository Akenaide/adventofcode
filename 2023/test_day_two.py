import pytest

import day_two


def test_split_game_num():
    entry = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert day_two.get_game_num(entry) == 1


def test_slit_sets():
    entry = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert day_two.get_sets(entry) == [
        {
            "blue": 3,
            "red": 4,
        },
        {
            "red": 1,
            "green": 2,
            "blue": 6,
        },
        {
            "green": 2,
        },
    ]


def test_possible_1():
    entry = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    config = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    assert day_two.is_possible(config, entry)


def test_not_possible_1():
    entry = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    config = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    assert not day_two.is_possible(config, entry)


def test_multiply():
    entry = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    assert day_two.get_power(entry) == 48
