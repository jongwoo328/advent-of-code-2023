result_numbers = []
result_score = []

def calculate(line, index):
    answer_str, numbers_str = map(lambda x: x.strip() ,line.split(':')[-1].split('|'))
    answer = list(map(int, filter(lambda x: x.isdigit(), map(lambda x:x.strip(), answer_str.split()))))
    numbers = list(map(int, filter(lambda x: x.isdigit(), map(lambda x:x.strip(), numbers_str.split()))))

    match_cnt = 0
    for n in numbers:
        if n in answer:
            match_cnt += 1
    result_score[index] = match_cnt
    for i in range(index + 1, index + 1 + match_cnt):
        result_numbers[i] += 1 * result_numbers[index]
    

with open("day4-2.input", "r") as f:
    lines = f.readlines()
    for _ in range(len(lines)):
        result_numbers.append(1)
        result_score.append(0)

    for index, line in enumerate(lines):
        calculate(line, index)

    print(sum(result_numbers))