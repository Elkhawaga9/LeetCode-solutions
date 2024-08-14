class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        def help(row,col):
            if  row>=n or col>=n or col<0:
                return float('inf')
            if row == n - 1:
                return matrix[row][col]
            if (row,col) in memo:
                return memo[(row,col)]
            downRight = help(row+1,col+1) + matrix[row][col]
            downLeft = help(row+1,col-1) + matrix[row][col]
            down = help(row+1,col) + matrix[row][col]
            ans = min(downRight,downLeft,down)
            memo[(row,col)] = ans
            return ans
        return min(help(0, col) for col in range(n))