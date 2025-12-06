class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = tuple(sorted(state)) # frozenset(state) (antigo)
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def get_path(self):
        path = []
        current_node = self
        
        while current_node.parent is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        
        return list(reversed(path))