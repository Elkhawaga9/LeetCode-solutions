class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def help(idx):
            if idx>=n:
                return 0
            points,brain = questions[idx]
            if idx in memo:
                return memo[idx]
            ans =  max(help(idx+brain+1) + points, help(idx+1))
            memo[idx] =ans
            return ans 
        return help(0)
        