from src.domain.action import Action

class Instance:
    def __init__(self, filename):
        self.filename = filename
        self.actions = []
        self.mapping = {}  # Dicionário str -> int
        self.reverse = {}  # Dicionário int -> str
        self.next_id = 1

        self.initial = set()       # Conjunto de inteiros
        self.goal = set()          # Conjunto de inteiros
        self.goal_complete = set() # Estado final inferido

    def get_id(self, literal):
        sign = 1
        name = literal
        if literal.startswith("~"):
            sign = -1
            name = literal[1:]
        
        if name not in self.mapping:
            self.mapping[name] = self.next_id
            self.reverse[self.next_id] = name
            self.next_id += 1
        
        return sign * self.mapping[name]
    
    def get_successor(self, state):
        succs = []
        for action in self.actions:
            if action.is_applicable(state):
                new_state = action.apply(state)
                succs.append((action, new_state))
        return succs

    def load(self):
        with open(self.filename, "r") as file:
            lines = [l.strip() for l in file.readlines() if l.strip()]

        goal_line = lines.pop()      # Remove a última linha (Goal)
        initial_line = lines.pop()   # Remove a penúltima linha (Initial)

        for i in range(0, len(lines), 3):
            name = lines[i]
            line_pre = lines[i+1]
            line_pos = lines[i+2]

            # Pré-condições
            precs = set()
            for p in line_pre.split(";"):
                if p.strip():
                    precs.add(self.get_id(p.strip()))

            # Efeitos
            adds = set()
            dels = set()
            for eff in line_pos.split(";"):
                eff = eff.strip()
                if eff:
                    eff_id = self.get_id(eff)
                    if eff_id < 0:
                        dels.add(abs(eff_id))
                    else:
                        adds.add(eff_id)

            self.actions.append(Action(name, precs, adds, dels))

        # 3. PROCESSAR ESTADO INICIAL
        for prop in initial_line.split(";"):
            if prop.strip():
                self.initial.add(self.get_id(prop.strip()))

        # Completa com negativos (Closed World Assumption)
        for prop_name, pid in self.mapping.items():
            if pid not in {abs(x) for x in self.initial}:
                self.initial.add(-pid)

        # 4. PROCESSAR GOAL
        for prop in goal_line.split(";"):
            if prop.strip():
                self.goal.add(self.get_id(prop.strip()))

        # 5. INFERIR GOAL COMPLETO
        self.goal_complete = self.infer_complete_goal()
    



    def infer_complete_goal(self):
        goal = set(self.goal)
        defined = {abs(x) for x in goal}
        all_props = list(self.mapping.items())
        
        # Nomes que estão positivos no goal
        pos_names = {self.reverse[v] for v in goal if v > 0}

        for name, pid in all_props:
            literal_pos = pid
            
            if pid not in defined:
                if name.startswith("on_"):
                    # Lógica simplificada: se não está explicitamente no goal, assumimos falso
                    goal.add(-pid)
                elif name.startswith("ontable_"):
                    goal.add(-pid)
                elif name.startswith("clear_"):
                    goal.add(-pid)
                elif name == "handempty":
                    # Geralmente queremos a mão vazia no final
                    goal.add(literal_pos)
                else:
                    goal.add(-pid)
        return goal