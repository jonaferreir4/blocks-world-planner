
def h0(state, instance):
    return 0


def _state_set(state):
    return set(state)


def _lit_name(instance, lit):
    return instance.reverse[abs(lit)]


def _name_to_pos_id(instance, name):
    return instance.mapping.get(name)

def h1(state, instance):
    s = _state_set(state)
    cost = 0

    for lit in instance.goal:
        if lit <= 0:
            continue
        name = _lit_name(instance, lit)
        if name.startswith("on_"):
            if lit not in s:
                cost += 1
    return cost


def h2(state, instance):
    s = _state_set(state)
    cost = 0

    for lit in instance.goal:
        if lit <= 0:
            continue
        name = _lit_name(instance, lit)
        if name.startswith("on_"):
            if lit not in s:
                cost += 1
                parts = name.split("_")
                if len(parts) >= 3:
                    _, a, b = parts[0], parts[1], parts[2]
                    hid = _name_to_pos_id(instance, f"holding_{a}")
                    cid = _name_to_pos_id(instance, f"clear_{b}")
                    
                    if hid is not None and hid not in s:
                        cost += 1
                    if cid is not None and cid not in s:
                        cost += 1
                else:
                    continue
    return cost


def h3(state, instance, max_depth=50):

    s = _state_set(state)
    goals = {g for g in instance.goal if g > 0}

    if goals.issubset(s):
        return 0

    layers = [set(s)]

    for depth in range(1, max_depth + 1):
        new_layer = set(layers[-1])

        for action in instance.actions:

            if action.preconditions.issubset(new_layer):

                new_layer |= action.add_effects

        layers.append(new_layer)
        if goals.issubset(new_layer):
            return depth


    return max_depth


def h4(state, instance, max_depth=50):

    s = _state_set(state)
    goals = {g for g in instance.goal if g > 0}

    if goals.issubset(s):
        return 0

    layers = [set(s)]
    for depth in range(1, max_depth + 1):
        new_layer = set(layers[-1])
        for action in instance.actions:
            if action.preconditions.issubset(new_layer):
                new_layer |= action.add_effects
        layers.append(new_layer)

        if goals.issubset(new_layer):
           
            needed = set(goals)
            count = 0
           
            for d in range(depth, 0, -1):
                layer_facts = layers[d]
           
                for action in instance.actions:
           
                    if action.add_effects & needed:
           
                        needed = (needed - action.add_effects) | action.preconditions
                        count += 1
                        if not needed:
                            return count
            return count

    return max_depth
