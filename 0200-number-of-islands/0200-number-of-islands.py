class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        n,m = len(grid),len(grid[0]) 
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        
        def valid(i,j):
            return 0<=i<n and  0<=j<m

        def dfs(i,j):
            if not valid(i,j) or grid[i][j]==0:
                return
            grid[i][j]='0'
            for dx,dy in directions:
                ii = i+dx
                jj = j+dy
                if valid(ii,jj) and grid[ii][jj] == '1':
                    dfs(ii,jj)

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
        return ans