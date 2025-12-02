from src.domain.node  import Node
from collections import deque

def bfs(instance):

    explored = set()
    frontier = deque()
    frontier_set = set()

    start = Node(instance.initial, None, None, g=0)
    frontier.append(start)
    frontier_set.add(start.state)
    

    num_generated = 0

    while frontier:
        node = frontier.popleft()
        frontier_set.remove(node.state)

        if node.state in explored:
            continue

        explored.add(node.state)

        # print(f"\n=== Estado atual === {num_generated}")
        # for lit in sorted(node.state, key=lambda x: abs(x)):
        #     name = instance.reverse[abs(lit)]
            # if lit > 0:
            #     print(f" {name}")
            # else:
            #     print(f" ~{name}")

        # Teste de objetivo: se o estado cobre o goal completo
        if instance.goal.issubset(node.state):
            print("\nObjetivo alcançado!")
            return node.get_path(), num_generated, len(explored)

        # Expansão
        sucessores = instance.get_successor(node.state)
        num_generated += len(sucessores)

        for action, successor in sucessores:
            succ_node = Node(successor, node, action, g=node.g + action.cost)

            if succ_node.state not in explored and succ_node.state not in frontier_set: # 
                frontier.append(succ_node)
                frontier_set.add(succ_node.state)


    # Se não encontrou solução
    return None, num_generated, len(explored)
