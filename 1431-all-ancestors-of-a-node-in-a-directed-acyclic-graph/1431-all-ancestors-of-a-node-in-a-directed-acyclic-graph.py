class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        graph = defaultdict(list)
        for f,t in edges:
            graph[t].append(f)
        def dfs(node):
            if node in ancestors:
                return ancestors[node]
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            return ancestors[node]
        ans = [[] for i in range(n)]
        for i in range(n):
            ans[i] = sorted(dfs(i))
        return ans
