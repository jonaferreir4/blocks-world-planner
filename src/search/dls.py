from src.domain.node import Node
from ..domain.stack import Stack

def DLS(instance, limit):

    def is_cycle(node):
        state = node.state
        while node.parent is not None:
            node = node.parent
            if state == node.parent.state:
                return True
            node = node.parent
        return False
    
    frontier = Stack()
    root = Node(instance.initial_state, None, None, 0, 0)
    frontier.push(root)
    result = "falha"

    num_generated = 0

    while not frontier.is_empty():
        node = frontier.pop()

        if instance.is_goal(node.state):
            return node.get_path(), num_generated
        
        if node.g >= limit:
            result = "cutoff"
        elif not is_cycle(node):
            for action, state in instance.successors(node.state):
                child_node = Node(state, node, action, node.g + 1, 0)
                frontier.push(child_node)
                num_generated += 1
                
    return result, num_generated