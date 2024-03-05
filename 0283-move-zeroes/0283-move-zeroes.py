class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        seeker = 0
        holder = 0
        while(seeker<len(nums) and holder<len(nums)):
            if(nums[seeker]!=0 and nums[holder]==0):
                nums[seeker],nums[holder] = nums[holder],nums[seeker]
            if(nums[holder]!=0):
                holder+=1
            
            seeker+=1
        