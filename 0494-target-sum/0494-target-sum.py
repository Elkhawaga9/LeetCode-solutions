class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def help(idx,current):
            if idx==n:
                if current==target:
                    return 1
                return 0
            if (idx,current) in dp:
                return dp[(idx,current)]
            dp[(idx,current)] = help(idx+1,current+nums[idx]) + help(idx+1,current-nums[idx])
            return dp[(idx,current)]
        return help(0,0)