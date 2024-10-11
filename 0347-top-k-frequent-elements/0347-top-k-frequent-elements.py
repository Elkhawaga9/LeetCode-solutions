from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxHeap = []
        for x in c:
            heappush(maxHeap,(-c[x],x))
        ans = []
        for _ in range(k):
            _,elem = heappop(maxHeap)
            ans.append(elem)
        return ans
        