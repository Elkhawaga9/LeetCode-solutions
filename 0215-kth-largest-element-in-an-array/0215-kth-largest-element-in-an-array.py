class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = [-10005] * k
        heapify(arr)
        for i in nums:
            if i > arr[0]:
                heappop(arr)
                heappush(arr,i)
        return arr[0]
    