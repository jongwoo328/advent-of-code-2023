with open("day13-1.input", "r") as f:
    lines = f.read().splitlines()

patterns = []
pattern = []

for line in lines:
    if len(line) == 0:
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line)

else:
    patterns.append(pattern)


def check_horizontal_reflection(pattern: list[str]):
    for i in range(1, len(pattern)):
        for j in range(i, len(pattern)):
            if i * 2 - j - 1 < 0:
                continue
            if pattern[j] != pattern[i * 2 - j - 1]:
                break
        else:
            return i
    else:
        return 0


def check_horizontal(pattern: list[str]):
    return check_horizontal_reflection(pattern) * 100


def check_vertical(pattern: list[str]):
    return check_horizontal_reflection(list(zip(*pattern)))


def calcuate_reflection(pattern):
    return check_horizontal(pattern) or check_vertical(pattern)


print(sum(map(calcuate_reflection, patterns)))
