import re
import pathlib

translation_table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
letter_digit = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

only_digit = re.compile(r"\d")
errors = [
    55205,
    54992,
    55130,
    54980,
]
good = 54985


def translate_to_digit(entry: str) -> str:
    results = ""
    matches = letter_digit.finditer(entry)
    for d in [match.group(1) for match in matches]:
        if not d.isnumeric():
            results += translation_table[d]
        else:
            results += d

    return results


def get_digits(entry: str) -> str:

    digits = translate_to_digit(entry)
    return digits[0] + digits[-1]


def main():
    total = 0

    f = open(
        pathlib.Path.joinpath(
            pathlib.Path(__file__).parent.resolve(), "input_day_one.txt"
        )
    )

    total = sum(int(get_digits(line.strip())) for line in f.readlines())
    if total != good:
        print("Not good")
    else:
        print(total)


if __name__ == "__main__":
    main()
