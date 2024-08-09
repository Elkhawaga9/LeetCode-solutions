class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        def help(cur):
            if cur==n:
                return 1
            elif cur >n:
                return 0 
            if cur in memo:
                return memo[cur]
            else:
                memo[cur] = help(cur+1)+help(cur+2)
                return memo[cur]
        return help(0)