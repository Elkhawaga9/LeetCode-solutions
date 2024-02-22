class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        ans = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
               tempans =  grid[i][j]+grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]
               tempans+= grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]
               ans = max(ans,tempans)
        return ans
