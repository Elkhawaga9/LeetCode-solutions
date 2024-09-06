class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root=[i for i in range(len(isConnected))]
        sz=[1 for _ in range(len(isConnected))]

        def find(x):
            if x == root[x]:
                return x

            root[x]=find(root[x])
            return root[x]

        def union(x,y):
            rootX=find(x)
            rootY=find(y)

            if rootX != rootY:
                if sz[rootX]>sz[rootY]:
                    root[rootY] = rootX
                    sz[rootX] += sz[rootY]
                else:
                    root[rootX] = rootY
                    sz[rootY] += sz[rootY]

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j or isConnected[i][j] == 0:
                    continue
                union(i,j)
        st=set()
        for val in root:
            st.add(find(val))

        return len(st)

        