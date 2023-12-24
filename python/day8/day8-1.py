nodes = {}
start_node = None

with open("day8-1.input", "r") as f:
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
        if node["name"] == "AAA":
            start_node = node

    is_end = False
    cnt = 0
    current_node = start_node
    while not is_end:
        for inst in instructions:
            if inst == "L":
                current_node = nodes[current_node["left"]]
            elif inst == "R":
                current_node = nodes[current_node["right"]]
            cnt += 1
            if current_node["name"] == "ZZZ":
                is_end = True

    print(cnt)
