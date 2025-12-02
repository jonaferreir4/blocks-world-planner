from src.search.dls import dls

def ids(instance, limit_start=0):
    limit = limit_start
    while True:
        found, expanded, node = dls(instance, limit)
        if found:
            return expanded, node.get_path()
        limit += 1
