def sub_and_add_by_turns(matrix: list[list[int]]) -> int:
    nums = list(zip(*matrix))[0]

    start = nums[0]
    for idx in range(len(nums)):
        if idx + 1 == len(nums):
            break

        if idx % 2 == 0:
            start -= nums[idx + 1]
        else:
            start += nums[idx + 1]

    return start


def calculate(line: list[int]) -> int:
    memo = [line[:]]

    while not all(map(lambda x: x == 0, memo[-1])):
        temp = []
        for idx, num in enumerate(memo[-1]):
            if (idx + 1) == len(memo[-1]):
                break

            temp.append(memo[-1][idx + 1] - num)
        memo.append(temp)

    return sub_and_add_by_turns(memo)


with open("day9-2.input", "r") as f:
    lines = list(map(lambda x: list(map(int, x.split(" "))), f.read().splitlines()))

    result = 0
    for line in lines:
        result += calculate(line)

    print(result)
