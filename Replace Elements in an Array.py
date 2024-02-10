class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict1 = {}  # to save value with its index
        for i in range (len(nums)):
            dict1[nums[i]]=i

        for x,y in operations:
            
            nums[dict1[x]] = y #go to index and put new value
            dict1[y]=dict1[x] #update the value with new value, but same index
        return nums
        
