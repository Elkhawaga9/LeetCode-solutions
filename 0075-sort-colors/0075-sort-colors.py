class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroes = 0
        ones = 0
        twos = 0
        for i in nums:
            if i == 0:
                zeroes += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        for i in range(len(nums)):
            if zeroes:
                nums[i] = 0
                zeroes -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos-=1        