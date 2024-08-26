class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        memo = {}
        def valid(x,y):
            return 0<=x<n and 0<=y<n
        def DFS(i,j,steps):
            if not valid(i,j):
                return 0
            if (i,j,steps) in memo:
                return memo[(i,j,steps)]
            if steps==k:
                return 1
            ans = 0
            for dx,dy in moves:
                nx = i+dx
                ny = j+dy
                ans += DFS(nx,ny,steps+1)/8
            memo[(i,j,steps)] = ans
            return ans
        return DFS(row,column,0)  

            
            
            
        
        