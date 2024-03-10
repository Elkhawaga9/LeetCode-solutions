class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)//2):
            t = nums[i]+nums[len(nums)-i-1]
            ans = max(ans,t)
        return ans