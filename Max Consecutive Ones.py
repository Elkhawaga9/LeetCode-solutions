class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp = 0
        mx = 0
        for i in nums:
            if i==1:
                tmp+=1
            else:
                mx = max(tmp,mx)
                tmp = 0
        mx = max(tmp,mx)
        return mx


        
