class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (((n)*(n+1))>>1)-sum(nums)