import heapq
from src.domain.node import Node
from src.utils.heuristics import h1

def a_star(instance):
    initial = Node(instance.initial, None, None, 0, h1(instance.initial, instance))
    goal_state = frozenset(instance.goal_complete)

    open_heap = []
    heapq.heappush(open_heap, initial)

    visited = {}

    expanded = 0

    while open_heap:
        node = heapq.heappop(open_heap)

        if node.state == goal_state:
            return expanded, node.get_path()

        if node.state in visited and visited[node.state] < node.g:
            continue

        visited[node.state] = node.g

        for action, new_state in instance.get_successor(node.state):
            g = node.g + 1
            h = h1(new_state, instance)
            child = Node(new_state, node, action.name, g, h)
            heapq.heappush(open_heap, child)

        expanded += 1

    return expanded, None
