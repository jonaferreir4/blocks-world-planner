import heapq
from src.domain.node import Node
from src.utils.heuristics import h1

def bidirectional_a_star(instance):
    start = Node(instance.initial, None, None, 0, h1(instance.initial, instance))
    goal = Node(instance.goal_complete, None, None, 0, 0)

    open_fwd = []
    heapq.heappush(open_fwd, start)
    dist_fwd = {start.state: 0}

    open_bwd = []
    heapq.heappush(open_bwd, goal)
    dist_bwd = {goal.state: 0}

    expanded = 0

    while open_fwd and open_bwd:
        if open_fwd[0].f < open_bwd[0].f:
            node = heapq.heappop(open_fwd)
            expanded += 1

            for action, new_state in instance.get_successor(node.state):
                g = node.g + 1

                if new_state not in dist_fwd or g < dist_fwd[new_state]:
                    h = h1(new_state, instance)
                    nd = Node(new_state, node, action.name, g, h)
                    dist_fwd[new_state] = g
                    heapq.heappush(open_fwd, nd)

                    if new_state in dist_bwd:
                        return expanded, nd.get_path()
        else:
            node = heapq.heappop(open_bwd)
            expanded += 1

            for action, new_state in instance.get_successor(node.state):
                g = node.g + 1

                if new_state not in dist_bwd or g < dist_bwd[new_state]:
                    h = h1(new_state, instance)
                    nd = Node(new_state, node, action.name, g, h)
                    dist_bwd[new_state] = g
                    heapq.heappush(open_bwd, nd)

                    if new_state in dist_fwd:
                        return expanded, nd.get_path()

    return expanded, None
