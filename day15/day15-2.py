with open('day15-2.input', 'r') as f:
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


boxes = dict()
total = 0
for step in steps:
    if '=' in step:
        k, v = step.split('=')
        num = hash(k, 0)

        if not boxes.get(num):
            boxes[num] = dict()
        boxes[num][k] = int(v)

    elif '-' in step:
        k, v = step.split('-')
        num = hash(k, 0)

        if not boxes.get(num):
            continue

        if k in boxes[num]:
            boxes[num].pop(k)

for box_num, box in boxes.items():
    order = 0
    for label, value in box.items():
        total += (box_num + 1) * (order + 1) * value
        order += 1

print(total)
