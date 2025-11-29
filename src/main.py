
class Instance(argv[1]):
    def __init__(self, filename):
        self.filename = filename
        self.actions = []
        self.initial = [] # Vetor de inteiros
        self.goal = [] # Vetor de inteiros
        self.goal_ = [] # Estado final para a busca bidirecional
        self.mapping = {} # Dicionário str -> int

        def load(self):
            # AQUI VAI A LÓGICA DE PARSEAR O ARQUIVO (STRIPS)
            # 1. Ler o arquivo
            # 2. Mapear strings (on_a_b) para inteiros (1, 2...) 
            # 3. Preencher self.initial e self.goal
            pass


# Representa um nó na árvore
class Node:
    def __init__(self, instace, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = cost
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        self.state == other.state
    
    def __hash__(self):
        return hash(tuple(self.state))
    
def h1(node, goal_state):
    # Exemplo: Número de proposições erradas (Distância de Hamming)
    # Deve comparar node.state com goal_state
    count = 0
    # Lógica de cálculo...
    return count


class Solvers:
    pass

def  iterative_deepening_dfs():
    pass

def dlf():
    pass

def bfs():
    pass

def a_star():
    pass

def bi_directional_search():
    pass
