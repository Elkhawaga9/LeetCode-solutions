class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        distance = [[float('inf')]*(m) for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    distance[i][j] = 0
                    q.append([i,j])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def valid(x,y):
            return x>=0 and x<n and y>=0 and y<m
        while q:
            i,j = q.popleft()
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if (valid(x,y) and (mat[x][y]) and distance[x][y]>distance[i][j]+1):
                    distance[x][y] = distance[i][j]+1
                    q.append([x,y])
        return distance