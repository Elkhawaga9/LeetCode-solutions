class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        mn = 0
        mx = 0
        for i in range(indexDifference,n):
            if nums[i-indexDifference]>nums[mx]:
                mx = i-indexDifference
            if nums[i-indexDifference]<nums[mn]:
                mn = i-indexDifference
            if abs(nums[mn]-nums[i])>=valueDifference:
                return [i,mn]
            if abs(nums[mx]-nums[i])>=valueDifference:
                return [i,mx]
        return [-1,-1] 
            
        