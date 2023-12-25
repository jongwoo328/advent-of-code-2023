with open('day16-2.input', 'r') as f:
    lines = list(map(list, f.read().splitlines()))

puzzle = lines
puzzle_visit = [['.' for _ in range(len(puzzle[0]))] for _ in range(len(puzzle))]
visited = set()

def get_changed_direction(r: int, c: int, prev_direction: str) -> tuple[str] | tuple[str, str]:
    mirror = puzzle[r][c]
    if prev_direction == 'right':
        if mirror == '\\':
            return ('down',)
        elif mirror == '/':
            return ('up',)
        elif mirror == '|':
            return ('up', 'down')
        elif mirror == '-':
            return ('right',)
        else:
            raise ValueError(f'Unknown mirror {mirror}')
    elif prev_direction == 'left':
        if mirror == '\\':
            return ('up',)
        elif mirror == '/':
            return ('down',)
        elif mirror == '|':
            return ('up', 'down')
        elif mirror == '-':
            return ('left',)
        else:
            raise ValueError(f'Unknown mirror {mirror}')
    elif prev_direction == 'up':
        if mirror == '\\':
            return ('left',)
        elif mirror == '/':
            return ('right',)
        elif mirror == '|':
            return ('up',)
        elif mirror == '-':
            return ('left', 'right')
        else:
            raise ValueError(f'Unknown mirror {mirror}')
    elif prev_direction == 'down':
        if mirror == '\\':
            return ('right',)
        elif mirror == '/':
            return ('left',)
        elif mirror == '|':
            return ('down',)
        elif mirror == '-':
            return ('left', 'right')
        else:
            raise ValueError(f'Unknown mirror {mirror}')
    else:
        raise ValueError(f'Unknown direction {prev_direction}')


def visit(r: int, c: int, r_to: int, c_to: int):
    if r == r_to:
        for j in range(c, c_to + 1):
            if j >= 0 and j < len(puzzle[0]):
                puzzle_visit[r][j] = '#'
    elif c == c_to:
        for i in range(r, r_to + 1):
            if i >= 0 and i < len(puzzle):
                puzzle_visit[i][c] = '#'


def get_next_position(r: int, c: int, direction: str) -> tuple[int, int] | None:
    start_r, start_c = r, c
    if direction == 'right':
        for j in range(c + 1, len(puzzle[r])):
            if puzzle[r][j] != '.':
                visit(start_r, start_c, r, j)
                return r, j
        else:
            visit(start_r, start_c, r, len(puzzle[0]) - 1)
            return
    elif direction == 'left':
        for j in range(c - 1, -1, -1):
            if puzzle[r][j] != '.':
                visit(r, j, start_r, start_c)
                return r, j
        else:
            visit(r, 0, start_r, start_c)
            return
    elif direction == 'up':
        for i in range(r - 1, -1, -1):
            if puzzle[i][c] != '.':
                visit(i, c, start_r, start_c)
                return i, c
        else:
            visit(0, c, start_r, start_c)
            return
    elif direction == 'down':
        for i in range(r + 1, len(puzzle)):
            if puzzle[i][c] != '.':
                visit(start_r, start_c, i, c)
                return i, c
        else:
            visit(start_r, start_c, len(puzzle) - 1, c)
            return
    
    raise ValueError(f'Unknown direction {direction}')


def go_beam(from_r: int, from_c: int, direction: str):
    next_pos = get_next_position(from_r, from_c, direction)
    if not next_pos:
        return
    
    next_r, next_c = next_pos
    next_directions = get_changed_direction(next_r, next_c, direction)

    for direction in next_directions:
        if not (next_r, next_c, direction) in visited:
            visited.add((next_r, next_c, direction))
            go_beam(next_r, next_c, direction)


def clear_visit():
    for i in range(len(puzzle_visit)):
        for j in range(len(puzzle_visit[i])):
            puzzle_visit[i][j] = '.'
    visited.clear()


def get_count_from_visit():
    count = 0
    for l in puzzle_visit:
        count += l.count('#')
    return count

count_max = 0
for i in range(len(puzzle)):
    go_beam(i, -1, 'right')
    count = get_count_from_visit()
    count_max = max(count_max, count)
    clear_visit()

for i in range(len(puzzle)):
    go_beam(i, len(puzzle[0]), 'left')
    count = get_count_from_visit()
    count_max = max(count_max, count)
    clear_visit()

for j in range(len(puzzle[0])):
    go_beam(-1, j, 'down')
    count = get_count_from_visit()
    count_max = max(count_max, count)
    clear_visit()

for j in range(len(puzzle[0])):
    go_beam(len(puzzle), j, 'up')
    count = get_count_from_visit()
    count_max = max(count_max, count)
    clear_visit()

print(count_max)
