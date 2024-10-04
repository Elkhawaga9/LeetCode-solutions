class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        @cache
        def dp(curr_length,paste):
            if curr_length==n:
                return 0
            if curr_length>n:
                return float('inf')

            option1 = 1 + dp(curr_length+paste,paste) #paste
            option2 = 2 + dp(curr_length*2,curr_length)#copy and paste 

            return min(option1, option2)
        ans = 1 + dp(1,1) 
        return ans