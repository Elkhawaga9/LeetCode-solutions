class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        def dp(row, col):
            if row == 1 or col == 1:
                return 1
            if obstacleGrid[row][col]==1:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            down = dp(row - 1, col)
            right = dp(row, col - 1)

            ans = down + right
            memo[(row, col)] = ans
            memo[(col, row)] = ans
            return ans
        return dp(m-1, n-1)