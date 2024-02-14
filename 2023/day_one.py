import re
import pathlib

only_digit = re.compile(r"\d")
def get_digits(entry: str) -> str:
    digits = only_digit.findall(entry)
    return digits[0] + digits[-1]

def main():
    sum = 0
    
    f = open(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), "input_day_one.txt" ))
    for line in f.readlines():
        sum += int(get_digits(line))
    print(sum)

if __name__ == "__main__":
    main()