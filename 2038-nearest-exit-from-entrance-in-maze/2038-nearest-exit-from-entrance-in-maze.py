class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        q = deque()
        q.append([entrance[0],entrance[1],0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        maze[entrance[0]][entrance[1]] ='+' 
        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        while(q):
            i,j,steps = q.popleft()
            for dx,dy in directions:
                x = i+dx
                y = j+dy
                if valid(x,y) and maze[x][y]=='.':
                    if x==0 or y==0 or x == m-1 or y == n-1:
                        return steps+1
                    maze[x][y] = '+'
                    q.append([x,y,steps+1])
        return -1


        