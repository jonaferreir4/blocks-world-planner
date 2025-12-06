from src.domain.node import Node
from ..domain.stack import Stack

def DLS(start_state, goal_state, limit):

    def is_cycle(node):
        state = node.state
        while node.parent is not None:
            node = node.parent
            if state == node.parent.state:
                return True
            node = node.parent
        return False
    
    frontier = Stack()
    frontier.push(Node(start_state, None, None, 0, 0))
    result = "falha"

    num_generated = 0

    while not frontier.is_empty():
        node = frontier.pop()

        if node.state == goal_state:
            return node.get_path(), num_generated
        
        if node.cost >= limit:
            result = "cutoff"
        elif not is_cycle(node):
            for action, state in enumerate(node.state.get_successors()):
                child_node = Node(state, node, action, node.g + 1, 0)
                frontier.push(child_node)
                num_generated += 1
                
    return result, num_generated