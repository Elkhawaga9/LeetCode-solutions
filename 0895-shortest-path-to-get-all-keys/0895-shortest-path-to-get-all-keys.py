from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        q = deque()
        visited = set()
        n, m = len(grid), len(grid[0])
        total_keys = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    q.append((i, j, 0, set()))  
                if grid[i][j].islower():
                    total_keys += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def valid(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j] != '#'

        while q:
            i, j, step, taken_keys = q.popleft()
            visited.add((i, j, frozenset(taken_keys)))

            if len(taken_keys) == total_keys:
                return step

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if valid(x, y):
                    cell = grid[x][y]
                    new_keys = set(taken_keys)

                    if cell.isupper() and cell.lower() not in taken_keys:
                        continue

                    if cell.islower():
                        new_keys.add(cell)

                    if (x, y, frozenset(new_keys)) not in visited:
                        visited.add((x, y, frozenset(new_keys)))
                        q.append((x, y, step + 1, new_keys))

        return -1