class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target= sum(nums)//2
        memo={}
        n=len(nums)
        def help(idx,curr_sum):
            if idx==n or curr_sum>target:
                return False
            if curr_sum == target:
                return True
            if (idx,curr_sum) in memo:
                return memo[(idx,curr_sum)]
            memo[(idx,curr_sum)] = help(idx+1,curr_sum) or help(idx+1,curr_sum+nums[idx])
            return memo[(idx,curr_sum)]        
        return help(0,0)