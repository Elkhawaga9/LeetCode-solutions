from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n 

        for start in range(n):
            if color[start] == 0: 
                queue = deque([start])
                color[start] = 1  

                while queue:
                    node = queue.popleft()
                    current_color = color[node]

                    for neighbor in graph[node]:
                        if color[neighbor] == 0:  
                            color[neighbor] = -current_color  
                            queue.append(neighbor)
                        elif color[neighbor] == current_color: 
                            return False  # The graph is not bipartite

        return True  

