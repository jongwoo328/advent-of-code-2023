digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_length_3 = ["one", "two", "six"]
digit_length_4 = ["four", "five", "nine"]
digit_length_5 = ["three", "seven", "eight"]


def word_to_digit(word: str) -> int:
    return digit_words.index(word) + 1


def get_first_digit(string: list[str]) -> int:
    length = len(string)

    for i in range(length):
        if string[i].isdecimal():
            return int(string[i])

        words_3 = "".join(string[i : i + 3])
        words_4 = "".join(string[i : i + 4])
        words_5 = "".join(string[i : i + 5])

        if i <= length - 3 and words_3 in digit_length_3:
            return word_to_digit("".join(words_3))
        elif i <= length - 4 and words_4 in digit_length_4:
            return word_to_digit("".join(words_4))
        elif i <= length - 5 and words_5 in digit_length_5:
            return word_to_digit("".join(words_5))


def get_second_digit(string: list[str]) -> int:
    length = len(string)

    for i in reversed(range(length)):
        if string[i].isdecimal():
            return int(string[i])

        words_3 = "".join(string[i - 2 : i + 1])
        words_4 = "".join(string[i - 3 : i + 1])
        words_5 = "".join(string[i - 4 : i + 1])

        if i >= 2 and words_3 in digit_length_3:
            return word_to_digit("".join(words_3))
        elif i >= 3 and words_4 in digit_length_4:
            return word_to_digit("".join(words_4))
        elif i >= 4 and words_5 in digit_length_5:
            return word_to_digit("".join(words_5))


def get_calibration_value(string: list[str]):
    calibration_value_list = list()

    calibration_value_list.append(get_first_digit(string))
    calibration_value_list.append(get_second_digit(string))

    return calibration_value_list[0] * 10 + calibration_value_list[1]


with open("day1-2.input", "r") as f:
    data = list(map(list, f.readlines()))

    print(sum(map(get_calibration_value, data)))
