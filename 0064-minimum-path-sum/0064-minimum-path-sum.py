class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dp(row, col):
            if row == 0 or col == 0:
                return float('inf')
            if (row, col) in memo:
                return memo[(row, col)]
            # move right
            right = dp(row, col-1)
            
            # move down

            down = dp(row-1, col)

            ans = min(right, down) 
            if ans == float('inf'):
                ans = 0
            ans += grid[m-row][n-col]
            memo[(row, col)] = ans
            return ans
        return dp(m, n)