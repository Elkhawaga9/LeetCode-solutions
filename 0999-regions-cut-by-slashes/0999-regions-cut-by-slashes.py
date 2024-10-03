class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            rootX=find(x)
            rootY=find(y)

            if rootX != rootY:
                if sz[rootX]>sz[rootY]:
                    parent[rootY] = rootX
                    sz[rootX] += sz[rootY]
                else:
                    parent[rootX] = rootY
                    sz[rootY] += sz[rootY]
                nonlocal ans
                ans-=1
                

        n = len(grid)
        ans = n * n * 4
        parent = list(range(ans))
        sz=[1 for _ in range(ans)]



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell_index = i * n + j
                if i < n - 1:
                    union(4 * cell_index + 2, 4 * (cell_index + n))
                if j < n - 1:
                    union(4 * cell_index + 1, 4 * (cell_index + 1) + 3)
              
                if grid[i][j] == '/':
                    union(4 * cell_index, 4 * cell_index + 3)
                    union(4 * cell_index + 1, 4 * cell_index + 2)
                elif grid[i][j] == '\\':
                    union(4 * cell_index, 4 * cell_index + 1)
                    union(4 * cell_index + 2, 4 * cell_index + 3)
                else:
                    union(4 * cell_index, 4 * cell_index + 1)
                    union(4 * cell_index + 1, 4 * cell_index + 2)
                    union(4 * cell_index + 2, 4 * cell_index + 3)

        return ans

