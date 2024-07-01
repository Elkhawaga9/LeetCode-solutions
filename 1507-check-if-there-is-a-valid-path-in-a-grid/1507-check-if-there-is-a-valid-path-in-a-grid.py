class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        visited = set()
        def dfs(i,j):
            if (i, j) in visited:
                return False
            if not (0 <= i < n and 0 <= j < m):
                return False
            
            visited.add((i, j))
            if i == n-1 and j == m-1:
                return True

            if grid[i][j]==1:
                return (j + 1 < m and (grid[i][j + 1] in [1, 3, 5]) and dfs(i, j + 1)) or \
                       (j - 1 >= 0 and (grid[i][j - 1] in [1, 4, 6]) and dfs(i, j - 1))
            elif grid[i][j]==2:
                return (i + 1 < n and (grid[i + 1][j] in [2, 5, 6]) and dfs(i + 1, j)) or \
                       (i - 1 >= 0 and (grid[i - 1][j] in [2, 3, 4]) and dfs(i - 1, j))
            elif grid[i][j]==3:
                return (j - 1 >= 0 and (grid[i][j - 1] in [1, 4, 6]) and dfs(i, j - 1)) or \
                       (i + 1 < n and (grid[i + 1][j] in [2, 5, 6]) and dfs(i + 1, j))
            elif grid[i][j]==4:
                return (j + 1 < m and (grid[i][j + 1] in [1, 3, 5]) and dfs(i, j + 1)) or \
                       (i + 1 < n and (grid[i + 1][j] in [2, 5, 6]) and dfs(i + 1, j))
            elif grid[i][j]==5:
                return (j - 1 >= 0 and (grid[i][j - 1] in [1, 4, 6]) and dfs(i, j - 1)) or \
                       (i - 1 >= 0 and (grid[i - 1][j] in [2, 3, 4]) and dfs(i - 1, j))
            elif grid[i][j]==6:
                return (j + 1 < m and (grid[i][j + 1] in [1, 3, 5]) and dfs(i, j + 1)) or \
                       (i - 1 >= 0 and (grid[i - 1][j] in [2, 3, 4]) and dfs(i - 1, j))
            return False
        return dfs(0,0)
        