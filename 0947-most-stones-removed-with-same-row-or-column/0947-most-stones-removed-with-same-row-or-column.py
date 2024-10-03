from collections import Counter
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        sz = [1]*(n)
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])  
            return parent[node]
        def union(u,v):
            par1,par2 = find(u),find(v)
            if par1==par2:
                return 
            if sz[par2]>sz[par1]:
                par1,par2 = par2,par1
            parent[par2] = par1
            sz[par1]+=sz[par2]

        for i in range(n):
            r1,c1 = stones[i]
            for j in range(n):
                r2,c2 = stones[j]
                if r1==r2 or c1==c2:
                    union(i,j)
        for i in range(n):
            find(i)
        s = Counter(parent)
        print(parent)
        print(s)
        return n-len(s)

        
