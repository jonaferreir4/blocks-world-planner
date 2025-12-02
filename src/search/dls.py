from src.domain.node import Node

def dls(instance, limit):

    def recursive(node, depth, expanded):
        if node.state == frozenset(instance.goal_complete):
            return True, expanded, node

        if depth == 0:
            return False, expanded, None

        for action, new_state in instance.get_successor(node.state):
            child = Node(new_state, node, action.name)
            found, expanded2, result = recursive(child, depth - 1, expanded + 1)

            if found:
                return True, expanded2, result

        return False, expanded, None

    start_node = Node(instance.initial)
    return recursive(start_node, limit, 0)
