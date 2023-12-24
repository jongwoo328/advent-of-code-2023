def calculate_power_of_fewest_cubes(game_data: dict) -> dict:
    game_steps = game_data["game_steps"]

    fewest_cubes = {"red": 0, "green": 0, "blue": 0}

    for step in game_steps:
        red = step.get("red", 0)
        green = step.get("green", 0)
        blue = step.get("blue", 0)

        if red > fewest_cubes["red"]:
            fewest_cubes["red"] = red
        if green > fewest_cubes["green"]:
            fewest_cubes["green"] = green
        if blue > fewest_cubes["blue"]:
            fewest_cubes["blue"] = blue

    return fewest_cubes["red"] * fewest_cubes["green"] * fewest_cubes["blue"]


with open("day2-1.input", "r") as f:
    data = f.readlines()

    def refine(game_data: str) -> dict:
        game_id = int(game_data.split(":")[0].split(" ")[-1])

        def refine_step(step: str) -> dict:
            colors = step.strip().split(",")
            total = dict()

            def split_color_and_number(each: str) -> dict:
                num_str, color = each.strip().split(" ")
                total[color] = int(num_str)

            for each_color in colors:
                split_color_and_number(each_color)

            return total

        game_steps = list(map(refine_step, game_data.split(":")[-1].strip().split(";")))

        return {"game_id": game_id, "game_steps": game_steps}

    refined_game_data = list(map(refine, data))

    result = sum(map(calculate_power_of_fewest_cubes, refined_game_data))
    print(result)
