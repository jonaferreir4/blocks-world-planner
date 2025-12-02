def h1(state, instance):
    count = 0

    goal_on = {
        instance.reverse[v]
        for v in instance.goal_complete
        if v > 0 and instance.reverse[v].startswith("on_")
    }

    state_on = {
        instance.reverse[v]
        for v in state
        if v > 0 and instance.reverse[v].startswith("on_")
    }

    for g in goal_on:
        if g not in state_on:
            count += 1

    return count
