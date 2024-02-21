class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l1 = [i for i in range(1, n + 1)]
        removed = 0
        while len(l1) > 1:
            #print(l1)
            #print(removed)
            removed = (removed+ k - 1) % len(l1)
            l1.remove(l1[removed])

        return l1[0]
