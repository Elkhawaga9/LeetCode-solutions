class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        id1 = -1
        id2 = -1
        # to find first decreasing from the right
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                id1 = i-1
                break
        if id1==-1:
            nums.reverse()
            return
        # to find the greater from the right
        for i in range(len(nums)-1,id1,-1):
            if nums[i]>nums[id1]:
                id2 = i
                break
        # swapping
        nums[id1],nums[id2] = nums[id2],nums[id1]

        i = id1+1
        j = len(nums)-1
        
        while(i<j):
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
