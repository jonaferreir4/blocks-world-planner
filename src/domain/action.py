class Action: 
    def __init__(self, name, preconditions, add_effects, del_effects, cost=1):
        self.name =  name
        self.preconditions = preconditions
        self.add_effects = add_effects
        self.del_effects = del_effects
        self.cost = cost

    def is_applicable(self, state): # Verifica se a ação pode ser aplicada ao estado
        return self.preconditions.issubset(state)
    
    def apply(self, state): # Aplica a ação ao estado e retorna o novo estado
        return (state - self.del_effects) | self.add_effects
