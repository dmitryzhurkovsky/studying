"""Graphs"""
from collections import deque

graph = {}
graph['i'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name: str) -> bool:
    return name[-1] == 'm'


def search() -> bool:
    """Isn't greedy algorithm"""
    search_queue = deque()
    search_queue += graph['i']
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
