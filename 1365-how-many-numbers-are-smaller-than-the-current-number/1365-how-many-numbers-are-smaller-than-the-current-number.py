class Solution:
   def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
      l1 = sorted(nums)
      ans = []
      for x in nums:
         ans.append(l1.index(x))
      return ans 
        