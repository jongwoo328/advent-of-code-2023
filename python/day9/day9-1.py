def calculate(line: list[int]) -> int:
    memo = [line[:]]

    while not all(map(lambda x: x == 0, memo[-1])):
        temp = []
        for idx, num in enumerate(memo[-1]):
            if (idx + 1) == len(memo[-1]):
                break

            temp.append(memo[-1][idx + 1] - num)
        memo.append(temp)

    return sum(map(lambda x: x[-1], memo))


with open("day9-1.input", "r") as f:
    lines = list(map(lambda x: list(map(int, x.split(" "))), f.read().splitlines()))

    result = 0
    for line in lines:
        result += calculate(line)

    print(result)
