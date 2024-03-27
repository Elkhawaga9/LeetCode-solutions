class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        all = 1
        zero = 0
        n = len(nums)
        for i in nums:
            if i==0:
                zero +=1
                continue
            all*=i
        if zero>1:
            nums = [0 for i in range(n)]
            return nums

        for i in range (len(nums)):
            if zero and nums[i]!=0:
                nums[i] = 0
                continue
            if nums[i] == 0:
                nums[i] = all
                continue
            nums[i] = all//nums[i]
        return nums