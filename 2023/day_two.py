import pathlib

def get_game_num(entry: str) -> int:
    return int(entry.split(":")[0].split()[1])


def get_sets(entry: str) -> list[dict]:
    sets = []
    string_sets = entry.split(":")[1].split(";")
    for _set in string_sets:
        parsed_set = {}
        for color in _set.split(","):
            info = color.split()
            parsed_set[info[1]] = int(info[0])
        sets.append(parsed_set)

    return sets


def is_possible(config: dict, entry: str) -> bool:
    is_possible = True
    sets = get_sets(entry=entry)
    for _set in sets:
        for color in _set:
            if _set[color] > config[color]:
                is_possible = False
    return is_possible



def main():
    total = 0
    config = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }   
    f = open(
        pathlib.Path.joinpath(
            pathlib.Path(__file__).parent.resolve(), "input_day_two.txt"
        )
    )

    total = sum(int(get_game_num(line.strip())) for line in f.readlines() if is_possible(config=config, entry=line))
   
    print(total)


if __name__ == "__main__":
    main()
