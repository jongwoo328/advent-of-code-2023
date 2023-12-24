result = 0
dy = [-1, 1, -1, 0, 1, -1, 0, 1]
dx = [0, 0, 1, 1, 1, -1, -1, -1]


def is_out(y, x, row, col):
    return y < 0 or x < 0 or y >= row or x >= col


def get_is_part(engine, i, j):
    for k in range(8):
        y = i + dy[k]
        x = j + dx[k]
        if is_out(y, x, len(engine), len(engine[0])):
            continue

        item = engine[y][x]
        if not item.isdigit() and item != ".":
            return True
    else:
        return False


def calculate(engine, engine_row, row_num):
    global result
    num = ""
    is_num = False
    is_part = False
    for idx, char in enumerate(engine_row):
        if not is_num and char.isdigit():
            is_num = True
            num += char
            is_part = get_is_part(engine, row_num, idx)

        elif is_num and char.isdigit():
            num += char
            if not is_part:
                is_part = get_is_part(engine, row_num, idx)

        else:
            is_num = False
            if is_part:
                result += int(num)
            num = ""
            is_part = False
    else:
        is_num = False
        if is_part:
            result += int(num)
        num = ""
        is_part = False


with open("day3-1.input", "r") as f:
    engine = []
    for line in f.readlines():
        engine.append([char for char in line.strip()])

    for idx, line in enumerate(engine):
        calculate(engine, line, idx)

    print(result)
