class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        v = []
        visited = [0 for i in range(6)]
        def backtrack(idx):
            if idx==len(nums):
                ans.append(v.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    v.append(nums[i])
                    visited[i]=1
                    backtrack(idx+1)
                    v.pop()
                    visited[i] = 0
        backtrack(0)
        return ans



        
        