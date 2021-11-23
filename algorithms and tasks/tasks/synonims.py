from __future__ import annotations

import datetime
from collections import defaultdict, deque
from dataclasses import dataclass, field

from memory_profiler import memory_usage


def decorator(func):
    def wrapper():
        start = datetime.datetime.now()
        result = func()
        print(datetime.datetime.now() - start)
        print(memory_usage())

        return result

    return wrapper


# Method 1
# My version
@decorator
def method1():
    def is_synonymous(start: str, value: str, graph: dict) -> bool:
        if start == value:
            return True

        search_queue = deque()
        searched = set()

        search_queue += graph[start]

        while search_queue:
            guess = search_queue.popleft()
            if guess == value:
                return True
            else:
                if guess not in searched:
                    search_queue += graph[guess]
                    searched.add(guess)

        return False

    with open('test.in') as input_file, open('out.in', 'w') as output_file:
        cases = int(input_file.readline())
        for _ in range(cases):
            graph = defaultdict(set)

            synonyms = int(input_file.readline())

            for _ in range(synonyms):
                node1, node2 = input_file.readline().lower().split()
                graph[node1].add(node2)
                graph[node2].add(node1)

            tests = int(input_file.readline())

            for _ in range(tests):
                first, second = input_file.readline().lower().split()
                if is_synonymous(first, second, graph):
                    output_file.write('synonyms\n')
                else:
                    output_file.write('different\n')


# Method 2
@decorator
def method2():
    ANSWERS = []

    def dfs(start: Node, value: Node, visited: set):
        visited.add(start)

        for node in start.nodes:
            if node == value or (node not in visited and dfs(node, value, visited)):
                return True
        return False

    @dataclass(eq=True, frozen=True)
    class Node:
        value: str = field(compare=True)
        nodes: set[Node] = field(compare=False, default_factory=set)

        def connect(self, node: Node) -> None:
            node.nodes.add(self)
            self.nodes.add(node)

        def is_synonyms(self, node: Node):
            if self == node:
                return True
            visited: set[Node] = set()
            return dfs(self, node, visited)

    with open("../../test.in", "r") as file:
        cases = int(file.readline())
        for _ in range(cases):
            graph: dict[str, Node] = {}
            synonyms = int(file.readline())
            for _ in range(synonyms):
                first, second = file.readline().lower().split()
                first_node = graph.get(first, Node(first))
                second_node = graph.get(second, Node(second))
                graph.update(
                    {
                        first: first_node,
                        second: second_node,
                    }
                )
                first_node.connect(second_node)
            tests = int(file.readline())
            for _ in range(tests):
                first, second = file.readline().lower().split()
                first_node = graph.get(first, Node(first))
                second_node = graph.get(second, Node(second))
                ANSWERS.append(
                    "synonyms"
                    if first_node.is_synonyms(second_node)
                    else "different"
                )

    with open("../../result.txt", "w") as file:
        file.write("\n".join(ANSWERS))
        file.write("\n")


method1()
method2()

