from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    
    visited = {}
    visited[source] = (0,0)
    queue = deque([source])
  
    while queue:
      node = queue.popleft()
      for neighbor, weight in graph[node]:
        if neighbor not in visited:
          visited[neighbor] = (visited[node][0] + weight, visited[node][1] + 1)
          queue.append(neighbor)
          
    return visited
  
    

    
    
def bfs_path(graph, source):
    parents = {source: None}
    queue = deque([source])
    while queue:
      current_node = queue.popleft()
      for neighbor in graph[current_node]:
          if neighbor not in parents:  
              parents[neighbor] = current_node  
              queue.append(neighbor)  
    return parents
    


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  if destination not in parents:
    return ''
  else:
    parent = parents[destination]
    return get_path(parents, parent) + parent

