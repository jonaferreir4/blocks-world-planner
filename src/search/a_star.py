import heapq
from src.domain.node import Node
from src.utils.heuristics import h0, h1, h2, h3, h4

def a_star(instance, heuristic=h0):
   

   explored = set()
   frontier = []
   frontier_set = set()
   num_generated = 0

   start_state = tuple(sorted(instance.initial))
   h0 = heuristic(start_state,instance)

   start_node = Node(start_state, None, None, g=0, h=h0)
   heapq.heappush(frontier, (start_node.f, start_node))
   frontier_set.add(start_node.state)


   while frontier:
      _, node = heapq.heappop(frontier)
      frontier_set.remove(node.state)

      if node.state in explored:
         continue
      
      explored.add(node.state)

      if instance.goal.issubset(node.state):
            print("\nObjetivo alcançado!")
            return node.get_path(), num_generated, len(explored)
      
      successors = instance.get_successor(node.state)
      num_generated += len(successors)


      for action, succ_state in successors:
          new_g = node.g + action.cost
          new_h = heuristic(succ_state, instance)

          child = Node(succ_state, node, action, g=new_g, h=new_h)

          if child.state not in explored and child.state not in frontier_set:
              heapq.heappush(frontier, (child.f, child))
              frontier_set.add(child.state)

   return  None, num_generated, len(explored)

