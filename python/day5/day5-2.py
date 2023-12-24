memos = {
    'seed' : dict(),
    'soil' : dict(),
    'fertilizer' : dict(),
    'water' : dict(),
    'light' : dict(),
    'temperature' : dict(),
    'humidity' : dict()
}

def get_value_from_map(input_data: int, map_dict: dict[tuple[int, int], int], type: str) -> int:
    if input_data in memos[type]:
        return memos[type][input_data]
    
    for (start, end), value in map_dict.items():
        if start <= input_data <= end:
            memos[type][input_data] = value + (input_data - start)
            return value + (input_data - start)
    else:
        memos[type][input_data] = input_data
        return input_data

def calculate(
    seed: int,
    seed_to_soil: dict[tuple[int, int], int],
    soil_to_fertilizer: dict[tuple[int, int], int],
    fertilizer_to_water: dict[tuple[int, int], int],
    water_to_light: dict[tuple[int, int], int],
    light_to_temperature: dict[tuple[int, int], int],
    temperature_to_humidity: dict[tuple[int, int], int],
    humidity_to_location: dict[tuple[int, int], int],
):
    seed_memo = dict()

    if seed in seed_memo:
        return seed_memo[seed]
    soil = get_value_from_map(seed, seed_to_soil, 'seed')
    fertilizer = get_value_from_map(soil, soil_to_fertilizer, 'soil')
    water = get_value_from_map(fertilizer, fertilizer_to_water, 'fertilizer')
    light = get_value_from_map(water, water_to_light, 'water')
    temperature = get_value_from_map(light, light_to_temperature, 'light')
    humidity = get_value_from_map(temperature, temperature_to_humidity, 'temperature')
    location = get_value_from_map(humidity, humidity_to_location, 'humidity')
    return location
            


def create_map(line_str):
    d = dict()
    for line in line_str.strip().split("\n"):
        dest, source, width = map(int, line.split(" "))
        d[(source, source + width)] = dest
    return d


with open("day5-2.input", "r") as f:
    file = f.read()
    seeds_str, rest = file.split("seed-to-soil map:")
    seed_to_soil_str, rest = rest.split("soil-to-fertilizer map:")
    soil_to_fertilizer_str, rest = rest.split("fertilizer-to-water map:")
    fertilizer_to_water_str, rest = rest.split("water-to-light map:")
    water_to_light_str, rest = rest.split("light-to-temperature map:")
    light_to_temperature_str, rest = rest.split("temperature-to-humidity map:")
    temperature_to_humidity_str, humidity_to_location_str = rest.split(
        "humidity-to-location map:"
    )

    seeds_list = []
    temp = []
    for seed in list(map(int, seeds_str.strip().split("seeds: ")[-1].split(" "))):
        if len(temp) == 0:
            temp.append(seed)
        elif len(temp) == 1:
            temp.append(seed)
            seeds_list.append([temp[0], temp[1]])
            temp = []

    seed_to_soil = create_map(seed_to_soil_str)
    soil_to_fertilizer = create_map(soil_to_fertilizer_str)
    fertilizer_to_water = create_map(fertilizer_to_water_str)
    water_to_light = create_map(water_to_light_str)
    light_to_temperature = create_map(light_to_temperature_str)
    temperature_to_humidity = create_map(temperature_to_humidity_str)
    humidity_to_location = create_map(humidity_to_location_str)

    min_location = float('inf')
    for (seed_start, seed_width) in seeds_list:
        for seed in range(seed_start, seed_start + seed_width + 1):

            location = calculate(
                seed,
                seed_to_soil,
                soil_to_fertilizer,
                fertilizer_to_water,
                water_to_light,
                light_to_temperature,
                temperature_to_humidity,
                humidity_to_location,
            )
            min_location = min(min_location, location)
    print(min_location)