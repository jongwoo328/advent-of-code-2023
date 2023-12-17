from itertools import combinations


magnification = 1_000_000


def get_dist(
    p1: tuple[int, int],
    p2: tuple[int, int],
    empty_columns: list[int],
    empty_rows: list[int],
) -> int:
    x1, y1 = p1
    x2, y2 = p2
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)

    for x in range(min(x1, x2), max(x1, x2) + 1):
        if x in empty_rows:
            dist_x = dist_x - 1 + magnification
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if y in empty_columns:
            dist_y = dist_y - 1 + magnification
    return dist_x + dist_y


with open("day11-2.input", "r") as f:
    universe = list(map(list, f.read().splitlines()))

    empty_columns = []
    empty_rows = []
    universe_columns = list(zip(*universe))

    galaxies = []
    for i in range(len(universe[0])):
        if all(map(lambda x: x == ".", universe_columns[i])):
            empty_columns.append(i)

    for i in range(len(universe)):
        if all(map(lambda x: x == ".", universe[i])):
            empty_rows.append(i)
        for j in range(len(universe[0])):
            if universe[i][j] == "#":
                galaxies.append((i, j))

    total = 0
    for p1, p2 in combinations(galaxies, 2):
        total += get_dist(p1, p2, empty_columns, empty_rows)

    print(total)
