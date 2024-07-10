from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        q = deque()
        q.append(['0000',0])
        visited = set()
        while q:
            current,steps = q.popleft()
            if current == target:
                return steps
            if current in visited or current in deadends:
                continue
            visited.add(current)
            for i in range(4):
                newc1 = current[:i]+str((int(current[i])+1)%10)+current[i+1:]
                newc2 = current[:i]+str((int(current[i])-1)%10)+current[i+1:]
                q.append([newc1,steps+1])
                q.append([newc2,steps+1])
        return -1
