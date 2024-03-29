from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        for i in range(1,n):
            nums[i]+=nums[i-1]
        for i in nums:
            if (i-k) in freq:
               ans+=freq[i-k]
            freq[i] += 1
        return ans