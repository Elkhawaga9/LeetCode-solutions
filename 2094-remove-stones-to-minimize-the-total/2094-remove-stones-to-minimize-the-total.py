class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-val for val in piles]
        heapify(piles)
        for _ in range(k):
            current = -1*heappop(piles)
            current = current-current//2
            heappush(piles,-current)
        return -1*sum(piles)
