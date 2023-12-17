dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_out(row: int, col: int, maze: list[list[str]]) -> bool:
    return row < 0 or row >= len(maze) or col < 0 or col >= len(maze[row])


def is_valid_direction(dy: int, dx: int, next_pipe: str) -> bool:
    if next_pipe == "S":
        return True
    if dy == -1 and dx == 0:
        if next_pipe in ("|", "7", "F"):
            return True
    elif dy == 0 and dx == 1:
        if next_pipe in ("-", "7", "J"):
            return True
    elif dy == 1 and dx == 0:
        if next_pipe in ("|", "J", "L"):
            return True
    elif dy == 0 and dx == -1:
        if next_pipe in ("-", "L", "F"):
            return True
    return False


def get_loop_from(row: int, col: int, maze: list[list[str]]) -> dict:
    loop = []

    start_row, start_col = row, col
    row_now, col_now = row, col
    new_row, new_col = row, col
    prev_direction = None

    while True:
        row_now, col_now = new_row, new_col
        loop.append((row_now, col_now))

        for i in range(4):
            if (
                (prev_direction == (-1, 0) and (dy[i], dx[i]) == (1, 0))
                or (prev_direction == (0, 1) and (dy[i], dx[i]) == (0, -1))
                or (prev_direction == (1, 0) and (dy[i], dx[i]) == (-1, 0))
                or (prev_direction == (0, -1) and (dy[i], dx[i]) == (0, 1))
            ):
                continue

            cur_pipe = maze[row_now][col_now]
            if (
                (cur_pipe == "|" and (dy[i], dx[i]) in ((0, 1), (0, -1)))
                or (cur_pipe == "-" and (dy[i], dx[i]) in ((1, 0), (-1, 0)))
                or (cur_pipe == "7" and (dy[i], dx[i]) in ((-1, 0), (0, 1)))
                or (cur_pipe == "J" and (dy[i], dx[i]) in ((0, 1), (1, 0)))
                or (cur_pipe == "L" and (dy[i], dx[i]) in ((1, 0), (0, -1)))
                or (cur_pipe == "F" and (dy[i], dx[i]) in ((0, -1), (-1, 0)))
            ):
                continue

            new_row = row_now + dy[i]
            new_col = col_now + dx[i]

            if not is_out(new_row, new_col, maze) and is_valid_direction(
                dy[i],
                dx[i],
                maze[new_row][new_col],
            ):
                prev_direction = (dy[i], dx[i])

                if (new_row, new_col) == (start_row, start_col):
                    return loop

                break


with open("day10-2.input", "r") as f:
    maze = list(map(lambda x: list(x), f.read().splitlines()))

    s_row, s_col = None, None
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "S":
                s_row, s_col = row, col
                break
        if s_row is not None and s_col is not None:
            break

    loop = get_loop_from(s_row, s_col, maze)

    start_adj = set()
    start_adj.add((loop[0][0] - loop[-1][0], loop[0][1] - loop[-1][1]))
    start_adj.add((loop[0][0] - loop[1][0], loop[0][1] - loop[1][1]))

    if start_adj == {(-1, 0), (1, 0)}:
        maze[s_row][s_col] = "|"
    elif start_adj == {(0, -1), (0, 1)}:
        maze[s_row][s_col] = "-"
    elif start_adj == {(1, 0), (0, -1)}:
        maze[s_row][s_col] = "L"
    elif start_adj == {(-1, 0), (0, -1)}:
        maze[s_row][s_col] = "F"
    elif start_adj == {(-1, 0), (0, 1)}:
        maze[s_row][s_col] = "7"
    elif start_adj == {(1, 0), (0, 1)}:
        maze[s_row][s_col] = "J"

    cross = 0
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in loop:
                if maze[i][j] == "|":
                    cross += 1
                elif maze[i][j] in ("L", "7"):
                    cross += 0.5
                elif maze[i][j] in ("F", "J"):
                    cross -= 0.5
            else:
                if cross % 2:
                    count += 1

        else:
            cross = 0
    print(count)
