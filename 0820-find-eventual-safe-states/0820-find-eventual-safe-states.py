class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        ans = []
        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for child in graph[node]:
                if not dfs(child):
                    return False
            safe[node] = True
            return True
 
        for i in range(n):
            if dfs(i):
                ans.append(i)
        
        return ans