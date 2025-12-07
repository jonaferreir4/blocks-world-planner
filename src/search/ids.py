from src.search.dls import dls

def ids(instance):
    max_depth = 30
    total_generated = 0

    while True:
        result, generated = dls(instance, max_depth)
        total_generated += generated

        if result != "cutoff":
            print(f"Profundidade atingida: {max_depth}")
            return result, total_generated, None
        elif result == "falha":
            return None, total_generated, None
        depth += 1