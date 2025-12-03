"""
Equipe: Jona Ferreira de Sousa - 539700
        Nicolas Mauricio
"""

import sys
from src.domain.instance import Instance
from src.search.a_star import a_star
from src.search.bfs import bfs
from src.search.ids import ids
from src.search.bidirectional_a_star import bidirectional_a_star
from src.utils.heuristics import h1, h2, h3, h4 
import time


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <instancia.txt>")
        exit(0)

    instance = Instance(sys.argv[1])
    instance.load() 

    # print(f"Instância carregada: {instance.filename}")
    # print(f"Número de ações: {len(instance.actions)}")
    # print(f"ações: {[action.name for action in instance.actions]}")

    # print(f"precondições: {[action.preconditions for action in instance.actions]}")
    # print(f"add_effects : {[action.add_effects for action in instance.actions]}")
    # print(f"del_effects : {[action.del_effects for action in instance.actions]}")


    # print(f"ids do estado: { instance.initial }")

    start_time = time.time()
    # plan, generated, explored = bfs(instance)
    plan, generated, explored = a_star(instance, h4)

    end_time = time.time()
    if plan:
        print("Plano encontrado:")
        for act in plan:
            print(act.name)
        
    else:
        print("Nenhuma solução encontrada.")

print("Número de estados gerados:", generated)
print("Número de estados explorados:", explored)
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")


