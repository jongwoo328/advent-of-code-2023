def get_calibration_value(string: list[str]):
    calibration_value_list = list()

    for char in string:
        if char.isdecimal():
            calibration_value_list.append(char)
            break

    for char in reversed(string):
        if char.isdecimal():
            calibration_value_list.append(char)
            break

    return int("".join(calibration_value_list))


with open("day1-1.input", "r") as f:
    data = list(map(list, f.readlines()))

    print(sum(map(get_calibration_value, data)))
