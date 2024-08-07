import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) 
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  
        while len(self.nums) > self.k:  
            heapq.heappop(self.nums)
        return self.nums[0]  

# Example usage:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
