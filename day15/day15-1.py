with open('day15-1.input', 'r') as f:
    line = f.read()

steps = line.split(',')

def hash(string: str, value: int) -> int:
    for char in string:
        if char == '\n':
            continue
        value += ord(char)
        value *= 17
        _, value = divmod(value, 256)

    return value

total = 0
for step in steps:
    total += hash(step, 0)

print(total)
