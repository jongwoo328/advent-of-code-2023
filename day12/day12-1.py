import re


def compare(position_has_question: str, position: str, numbers: list[int]):
    if len(position_has_question) != len(position):
        return False

    position_pattern = list(map(lambda x: x.count("#"), re.split(r"\.+", position)))
    if position_pattern[0] == 0:
        position_pattern = position_pattern[1:]
    if position_pattern[-1] == 0:
        position_pattern = position_pattern[:-1]
    if position_pattern != numbers:
        return False

    for i in range(len(position_has_question)):
        char_q = position_has_question[i]
        char_r = position[i]
        if char_q == "?" or char_q == char_r:
            continue
        return False
    else:
        return True


def distribute_dot_case(dot_count: int, distribute_count: int):
    if distribute_count == 1:
        yield (dot_count,)
    else:
        for i in range(dot_count + 1):
            for comb in distribute_dot_case(dot_count - i, distribute_count - 1):
                yield (i, *comb)


def validate_case(code: str, numbers: list[int], dots: tuple[int]) -> bool:
    if len(dots) != len(numbers) + 1:
        return False
    created_code = ""
    for idx, number in enumerate(numbers):
        created_code += "." * dots[idx]
        created_code += "#" * number
    created_code += "." * dots[-1]

    return compare(code, created_code, numbers)


def calculate(code: str, numbers: list[int]) -> int:
    dot_count = len(code) - sum(numbers)

    count = 0
    for dot_comb in distribute_dot_case(dot_count, len(numbers) + 1):
        if validate_case(code, numbers, dot_comb):
            count += 1
    return count


with open("day12-1.input", "r") as f:
    spring_codes = f.read().splitlines()
    spring_codes = list(map(lambda x: x.split(" "), spring_codes))

    total = 0

    for code, numbers in spring_codes:
        numbers = list(map(int, numbers.split(",")))
        total += calculate(code, numbers)

    print(total)
