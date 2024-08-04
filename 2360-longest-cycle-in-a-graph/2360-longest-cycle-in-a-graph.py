class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
        visited = set()
        ans = -1
        def dfs(node,steps):
            nonlocal ans
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child,steps+1)
                else:
                    ans = max(ans,steps)         
             

        for i in range(len(edges)):
            if i not in visited:
                dfs(i,0)
        return ans