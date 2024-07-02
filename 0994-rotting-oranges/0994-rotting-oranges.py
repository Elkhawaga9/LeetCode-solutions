class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ans = -1
        def valid(x,y):
            return 0<=x<n and 0<=y<m
        while q:
            i,j,minutes = q.popleft()
            ans = minutes
            for dx,dy in directions:
                x = i+dx
                y = j+dy
                if valid(x,y) and grid[x][y] == 1:
                    grid[x][y]=2
                    q.append((x,y,minutes+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return 0 if ans == -1 else ans



