""""""
"Create and populated graph"
graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'finish': 1
    },
    'b': {
        'a': 3,
        'finish': 5
    },
    'finish': {}
}

"Create table of all nodes costs"

costs = {
    'a': 6,
    'b': 2,
    'finish': float('inf')
}

"Create parents table"
parents = {
    'a': 'start',
    'b': 'start',
    'finish': None
}

processed = []


def find_lowest_cost_node(costs: dict) -> str:
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


"""Isn't greedy algorithm"""
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

