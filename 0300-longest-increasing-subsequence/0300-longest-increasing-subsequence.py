class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [0]*(n)
        LIS[n-1] = 1
        for i in range(n-2,-1,-1):
            LIS[i] = LIS[i+1] + int(nums[i]<nums[i+1])
        return LIS[0]
            


        