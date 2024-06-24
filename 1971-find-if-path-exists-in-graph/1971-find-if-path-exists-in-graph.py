class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n) ]
        visited = [False for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            if node == destination:
                return True

            for l in adj[node]:
                if not visited[l]:
                    visited[l] = True
                    if dfs(l):
                        return True
                    visited[l] = False
            return False
        return dfs(source)
        