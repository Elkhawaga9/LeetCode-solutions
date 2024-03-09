class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        c = 0

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=(len(nums)-i)
        return c