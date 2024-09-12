class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
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
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i,j)
        ans= 0
        for i in range(n):
            if parent[i]==i:
                ans+=1
        return ans
        

        