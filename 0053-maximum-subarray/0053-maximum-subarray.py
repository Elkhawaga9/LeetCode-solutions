class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        mx = -10000
        curr_sum = 0
        for i in range(n):
            curr_sum+=nums[i]
            if curr_sum>mx:
                mx = curr_sum
            if curr_sum <0:
                curr_sum=0
        return mx