from math import sqrt
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        took = abs(target[0])+abs(target[1])
        for l1 in ghosts:
            if abs(l1[0] - target[0]) + abs(l1[1] - target[1]) <= took:
                return False
        return True
