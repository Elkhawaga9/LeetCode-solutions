class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*(len(rooms))
        q = deque([0])
        while q:
            node = q.popleft()
            visited[node] = True
            for child in rooms[node]:
                if not visited[child]:
                    q.append(child)
        for x in visited:
            if not x:
                return False
        return True
        