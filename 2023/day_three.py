import pathlib


def get_nums(entry: str) -> list:
    result = []
    tmp = ""
    start = None
    for i, charac in enumerate(entry):
        if charac.isdigit():
            tmp += charac
            if start is None:
                start = i
        else:
            if tmp:
                result.append((tmp, (start, i)))
                tmp = ""
                start = None
    if tmp:
        result.append((tmp, (start, i)))
        tmp = ""
        start = None
    return result


def check_lines(lines: list) -> bool:
    is_valid = False
    for line in lines:
        for val in line:
            if not val.isdigit() and val != ".":
                is_valid = True
    return is_valid


def valide_num(entry: list) -> list:
    nums = []
    for i, line in enumerate(entry):
        if i != 0:
            previous_line = entry[i - 1]
        else:
            previous_line = line
        if i != len(entry) - 1:
            next_line = entry[i + 1]
        else:
            next_line = line

        found_nums = get_nums(line)
        for found_num, indexes in found_nums:

            start_index = indexes[0]
            end_index = indexes[1] + 1  # +1 for diagonal
            if start_index != 0:
                start_index -= 1  # -1 for diagonal

            if check_lines(
                [
                    previous_line[start_index:end_index],
                    line[start_index:end_index],
                    next_line[start_index:end_index],
                ],
            ):
                nums.append(int(found_num))

    return nums


def main():
    total = 0
    f = open(
        pathlib.Path.joinpath(
            pathlib.Path(__file__).parent.resolve(), "input_day_three.txt"
        )
    )

    lines = [line.strip() for line in f.readlines()]
    print(valide_num(lines))

    print(sum(valide_num(lines)))
    # 557705


if __name__ == "__main__":
    main()
