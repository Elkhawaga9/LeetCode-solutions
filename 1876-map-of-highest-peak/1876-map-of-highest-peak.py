class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m = len(isWater),len(isWater[0])
        has = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if isWater[i][j]==1:
                    isWater[i][j]=0
                    has.append([i,j])
                else:
                    isWater[i][j] = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def valid(x,y):
            return 0 <= x < n and 0 <= y < m
        while has:
            i,j = has.popleft()
            for dx,dy in directions:
                x = i+dx
                y = j+dy
                if valid(x,y) and isWater[x][y]!=0 and (x,y) not in visited:
                    isWater[x][y] = isWater[i][j] + 1
                    has.append([x,y])
                    visited.add((x,y))
                 
        return isWater



        