max_count = {"red": 12, "green": 13, "blue": 14}


def get_game_id_if_possible(game_data: dict) -> int:
    game_id, game_steps = game_data["game_id"], game_data["game_steps"]

    for step in game_steps:
        red = step.get("red", 0)
        green = step.get("green", 0)
        blue = step.get("blue", 0)

        if (
            red > max_count["red"]
            or green > max_count["green"]
            or blue > max_count["blue"]
        ):
            return 0
    else:
        return game_id


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

    print(sum(map(get_game_id_if_possible, refined_game_data)))
