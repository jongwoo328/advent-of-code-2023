result_list = []

def calculate(line):
    global result_list
    answer_str, numbers_str = map(lambda x: x.strip() ,line.split(':')[-1].split('|'))
    answer = list(map(int, filter(lambda x: x.isdigit(), map(lambda x:x.strip(), answer_str.split()))))
    numbers = list(map(int, filter(lambda x: x.isdigit(), map(lambda x:x.strip(), numbers_str.split()))))
    
    score = 0
    for num in numbers:
        if num in answer:
            if score == 0:
                score = 1
            else:
                score *= 2
    result_list.append(score)
    
with open("day4-1.input", "r") as f:
    for line in f.readlines():
        calculate(line)
    
    result = 0
    score = 1
    print(sum(result_list))