class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        def calcDistance(x1,y1,x2,y2):
            return (x2-x1)**2 + (y2-y1)**2 
        graph = defaultdict(list)
        for i in range(n):
            x1,y1,r1 = bombs[i]
            for j in range(n):
                if i==j:
                    continue
                x2,y2,r2 = bombs[j]
                if calcDistance(x1,y1,x2,y2)<=r1**2:
                    graph[i].append(j)
        visited=set()
        def dfs(node):
            visited.add(node)
            c = 1
            for child in graph[node]:
                if child not in visited:
                    c += dfs(child)
            return c
            

        ans = 1
        for i in range(n):
            visited.clear()
            tmp = dfs(i)
            ans = max(tmp,ans)
        return ans