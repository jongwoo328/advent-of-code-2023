from itertools import combinations


def get_dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


with open("day11-1.input", "r") as f:
    universe = list(map(list, f.read().splitlines()))

    empty_columns = []
    empty_rows = []
    universe_columns = list(zip(*universe))

    for i in range(len(universe[0])):
        if all(map(lambda x: x == ".", universe_columns[i])):
            empty_columns.append(i)

    for i in range(len(universe)):
        if all(map(lambda x: x == ".", universe[i])):
            empty_rows.append(i)

    expanded_universe_temp = []
    expanded_universe = []
    for row in universe:
        new_row = row.copy()
        for index in reversed(empty_columns):
            new_row.insert(index, ".")
        expanded_universe_temp.append(new_row)

    for i, row in enumerate(expanded_universe_temp):
        if i in empty_rows:
            new_row = ["."] * len(expanded_universe_temp[0])
            expanded_universe.append(new_row)
            expanded_universe.append(new_row)
        else:
            expanded_universe.append(row.copy())

    galaxies = []
    for i in range(len(expanded_universe)):
        for j in range(len(expanded_universe[0])):
            if expanded_universe[i][j] == "#":
                galaxies.append((i, j))

    total = 0
    for p1, p2 in combinations(galaxies, 2):
        total += get_dist(p1, p2)

    print(total)
