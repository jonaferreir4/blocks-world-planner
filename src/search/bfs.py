from collections import deque
from src.domain.node import Node

def bfs(instance):

    # Nó raiz
    root = Node(instance.initial, parent=None, action=None, g=0)

    # Fila FIFO
    frontier = deque([root])

    # Conjunto de visitados
    explored = set()

    num_generated = 0

    goal = frozenset(instance.goal_complete)

    while frontier:
        node = frontier.popleft()  # Retira da fila

        explored.add(node.state)

        # Teste de objetivo
        if node.state == goal:
            return node.get_path(), num_generated

        # Expandir
        for action, new_state in instance.get_successor(node.state):
            num_generated += 1
            new_state_frozen = frozenset(new_state)

            if new_state_frozen not in explored:
                child = Node(
                    state=new_state_frozen,
                    parent=node,
                    action=action,
                    g=node.g + 1,
                    h=0
                )
                frontier.append(child)

    return None, num_generated
