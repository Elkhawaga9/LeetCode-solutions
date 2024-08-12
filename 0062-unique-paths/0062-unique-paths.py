class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            if row == 1 or col == 1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            down = dp(row - 1, col)
            right = dp(row, col - 1)

            ans = down + right
            memo[(row, col)] = ans
            memo[(col, row)] = ans
            return ans
        return dp(m, n)