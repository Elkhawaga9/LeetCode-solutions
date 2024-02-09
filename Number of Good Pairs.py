class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        answer = 0
        
        #iterating to update answer if the elements are equal
        for first in range(len(nums)):
            for second in range (first+1,len(nums)):
                if nums[first]==nums[second]:
                    answer+=1

        return answer 
        
