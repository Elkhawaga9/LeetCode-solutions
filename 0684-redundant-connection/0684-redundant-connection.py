class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        sz = [1]*(n+1)
        def find(node):
            if node == parent[node]:
                return node
            return find(parent[node])
        def union(u,v):
            par1,par2 = find(u),find(v)
            if par1==par2:
                return 
            if sz[par2]>sz[par1]:
                par1,par2 = par2,par1
            parent[par2] = par1
            sz[par1]+=sz[par2]
        for u,v in edges:
            if find(u)==find(v):
                return [u,v]
            else:
                union(u,v)