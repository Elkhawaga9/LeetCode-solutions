class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in nums:
            if i!=ans:
                break
            else:
                ans+=1
        return ans 
        
