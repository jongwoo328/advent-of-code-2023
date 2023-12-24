with open('day14-1.input', 'r') as f:
    lines = f.read().splitlines()

dish = list(map(list, lines))

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

total = 0
for i in range(len(dish) - 1, -1, -1):
    score = len(dish) - i
    total += dish[i].count('O') * score

print(total)
