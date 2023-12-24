gear_dict = {}
result = 0
dy = [-1, 1, -1, 0, 1, -1, 0, 1]
dx = [0, 0, 1, 1, 1, -1, -1, -1]


def mul(items: list[int]):
    result = 1
    for item in items:
        result *= item
    return result


def is_out(y, x, row, col):
    return y < 0 or x < 0 or y >= row or x >= col


def get_gear_adj(engine, i, j):
    for k in range(8):
        y = i + dy[k]
        x = j + dx[k]
        if is_out(y, x, len(engine), len(engine[0])):
            continue

        item = engine[y][x]
        if item == "*":
            return (y, x)


def calculate(engine, engine_row, row_num):
    num = ""
    is_num = False
    gear_adj = None
    for idx, char in enumerate(engine_row):
        # 숫자 처음
        if not is_num and char.isdigit():
            is_num = True
            num += char
            gear_adj = get_gear_adj(engine, row_num, idx)

        # 숫자 중간
        elif is_num and char.isdigit():
            num += char
            if not gear_adj:
                gear_adj = get_gear_adj(engine, row_num, idx)

        # 나머지경우
        else:
            is_num = False
            if gear_adj:
                if not gear_dict.get(gear_adj):
                    gear_dict[gear_adj] = []
                gear_dict[gear_adj].append(int(num))
            num = ""
            gear_adj = None
    else:
        is_num = False
        if gear_adj:
            if not gear_dict.get(gear_adj):
                gear_dict[gear_adj] = []
            gear_dict[gear_adj].append(int(num))
        num = ""
        gear_adj = None


with open("day3-2.input", "r") as f:
    engine = []
    for line in f.readlines():
        engine.append([char for char in line.strip()])

    for idx, line in enumerate(engine):
        calculate(engine, line, idx)

    for pos, values in gear_dict.items():
        if len(values) > 1:
            result += mul(values)

    print(result)
