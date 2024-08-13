class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def help(idx):
            if idx==n-1:
                return nums[idx]
            if idx==n:
                return 0
            if idx in memo:
                return memo[idx]
            With = help(idx+2) + nums[idx]
            Without = help(idx+1)
            ans = max(With,Without)
            memo[idx] = ans
            return ans

        return help(0)
        