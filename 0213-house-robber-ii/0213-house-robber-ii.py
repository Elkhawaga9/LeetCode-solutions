class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def help(idx,end,memo):
            if idx>=end:
                return 0
            if idx in memo:
                return memo[idx]
            With = help(idx+2,end,memo) + nums[idx]
            Without = help(idx+1,end,memo)
            ans = max(With, Without)
            memo[idx] = ans
            return ans
        return max(help(0,n-1,{}),help(1,n,{}))      