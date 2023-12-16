from math import gcd

nodes = {}
start_nodes = []


def lcm(nums):
    lcm = nums[0]
    for i in nums[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


with open("day8-2.input", "r") as f:
    data = f.readlines()
    instructions = data[0].strip()

    def refine(instruction):
        from_node, to_nodes = list(map(lambda x: x.strip(), instruction.split("=")))
        left, right = map(
            lambda x: x.strip(), to_nodes.lstrip("(").rstrip(")").split(",")
        )
        return {
            "name": from_node,
            "left": left,
            "right": right,
        }

    refined_input = list(map(refine, map(lambda x: x.strip(), data[2:])))
    for node in refined_input:
        nodes[node["name"]] = node
        if node["name"].endswith("A"):
            start_nodes.append(node)

    is_end = False
    cnt = 0
    current_nodes = start_nodes[:]
    first_end_count = [0 for _ in current_nodes]
    while not is_end:
        for inst in instructions:
            if inst == "L":
                for idx, current_node in enumerate(current_nodes):
                    current_nodes[idx] = nodes[current_node["left"]]
            elif inst == "R":
                for idx, current_node in enumerate(current_nodes):
                    current_nodes[idx] = nodes[current_node["right"]]
            cnt += 1

            for idx, current_node in enumerate(current_nodes):
                if current_node["name"].endswith("Z") and first_end_count[idx] == 0:
                    first_end_count[idx] = cnt

            if all(map(lambda x: x != 0, first_end_count)):
                is_end = True
                break

    print(lcm(first_end_count))
