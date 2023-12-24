with open('day14-2.input', 'r') as f:
    lines = f.read().splitlines()

dish = list(map(list, lines))
def tilt_north(dish):
    for c in range(len(dish[0])):
        for r in range(len(dish)):
            if dish[r][c] != 'O':
                continue
            
            rock_position = (r, c)
            new_rock_position = (r, c)
            for i in range(r - 1, -2, -1):
                if i < 0 or dish[i][c] == 'O' or dish[i][c] == '#':
                    new_rock_position = (i + 1, c)
                    break
            
            if rock_position != new_rock_position:
                nr, nc = new_rock_position
                r, c = rock_position
                dish[nr][nc] = 'O'
                dish[r][c] = '.'

def tilt_south(dish):
    for c in range(len(dish[0])):
        for r in range(len(dish) - 1, -1, -1):
            if dish[r][c] != 'O':
                continue
            
            rock_position = (r, c)
            new_rock_position = (r, c)
            for i in range(r + 1, len(dish) + 1):
                if i >= len(dish) or dish[i][c] == 'O' or dish[i][c] == '#':
                    new_rock_position = (i - 1, c)
                    break
            if rock_position != new_rock_position:
                nr, nc = new_rock_position
                r, c = rock_position
                dish[nr][nc] = 'O'
                dish[r][c] = '.'

def tilt_west(dish):
    for r in range(len(dish)):
        for c in range(len(dish[0])):
            if dish[r][c] != 'O':
                continue

            rock_position = (r, c)
            new_rock_position = (r, c)
            for i in range(c - 1, -2, -1):
                if i < 0 or dish[r][i] == 'O' or dish[r][i] == '#':
                    new_rock_position = (r, i + 1)
                    break

            if rock_position != new_rock_position:
                nr, nc = new_rock_position
                r, c = rock_position
                dish[nr][nc] = 'O'
                dish[r][c] = '.'

def tilt_east(dish):
    for r in range(len(dish)):
        for c in range(len(dish[0]) -1, -1, -1):
            if dish[r][c] != 'O':
                continue

            rock_position = (r, c)
            new_rock_position = (r, c)
            for i in range(c + 1, len(dish[0]) + 1):
                if i >= len(dish[0]) or dish[r][i] == 'O' or dish[r][i] == '#':
                    new_rock_position = (r, i - 1)
                    break

            if rock_position != new_rock_position:
                nr, nc = new_rock_position
                r, c = rock_position
                dish[nr][nc] = 'O'
                dish[r][c] = '.'

def print_dish():
    for l in dish:
        print(l)

memo = dict()
loop = 1000000000 * 4

k = ''
n = 0
for n in range(loop):
    k = ''.join(map(''.join, dish))
    
    if k in memo:
        break
    
    memo[k] = n

    if n % 4 == 0:
        tilt_north(dish)
    elif n % 4 == 1:
        tilt_west(dish)
    elif n % 4 == 2:
        tilt_south(dish)
    else:
        tilt_east(dish)

period = n - memo[k]
_, rest = divmod(loop - memo[k], period)
for n2 in range(n, n + rest):
    if n2 % 4 == 0:
        tilt_north(dish)
    elif n2 % 4 == 1:
        tilt_west(dish)
    elif n2 % 4 == 2:
        tilt_south(dish)
    else:
        tilt_east(dish)

total = 0
for i in range(len(dish) - 1, -1, -1):
    score = len(dish) - i
    total += dish[i].count('O') * score

print(total)
