import re

with open("day6-1.input", "r") as f:
    data = f.readlines()
    times = list(map(int, re.split(r"\s+", data[0].strip().split(":")[-1].strip())))
    distances = list(map(int, re.split(r"\s+", data[1].strip().split(":")[-1].strip())))

    result = 1
    for time, distance in zip(times, distances):
        cnt = 0
        for hold in range(1, time + 1):
            speed_per_ms = hold
            record = distance / speed_per_ms
            if record < time - hold:
                cnt += 1
        else:
            result *= cnt

    print(result)
