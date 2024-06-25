from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj =defaultdict(list)
        visited = [False for _ in range(numCourses)]
        for a,b in prerequisites:
            if a==b:
                return False
            adj[a].append(b)
        
        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for pre in adj[node]:
                if not dfs(pre):
                   return False
            visited[node] = False
            return True
        
        for x in visited:
            if not x:
                if not dfs(x):
                    return False
        return True


        