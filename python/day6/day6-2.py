import re
import math


def binary_search(get_total_race_time, race_time_before: int, left: int, right: int):
    while left < right:
        hold_time = (left + right) // 2
        if get_total_race_time(hold_time) > race_time_before:
            left = hold_time + 1
        else:
            right = hold_time
    return left


def binary_search_max(
    get_total_race_time, race_time_before: int, left: int, right: int
):
    while left < right:
        hold_time = (left + right) // 2
        if get_total_race_time(hold_time) < race_time_before:
            left = hold_time + 1
        else:
            right = hold_time
    return left - 1


with open("day6-2.input", "r") as f:
    data = f.readlines()
    race_time = int("".join(re.split(r"\s+", data[0].strip().split(":")[-1].strip())))
    race_distance = int(
        "".join(re.split(r"\s+", data[1].strip().split(":")[-1].strip()))
    )

    def get_total_race_time(hold_time):
        speed = hold_time
        total_time = math.ceil(race_distance / speed)
        if total_time <= race_time - hold_time:
            return total_time
        else:
            return float("inf")

    min_value = binary_search(get_total_race_time, race_time, 1, race_time)
    max_value = binary_search_max(get_total_race_time, race_time, 1, race_time)
    print(max_value - min_value + 1)
