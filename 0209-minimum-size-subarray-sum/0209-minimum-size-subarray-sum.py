class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = 1000000000
        p = 0
        n = len(nums)
        tempSum = 0
        for i in range(n):
            while (p<n and tempSum<target):
                tempSum+=nums[p]
                p+=1
            if tempSum>=target:
                ans = min(ans,p-i)
            tempSum-=nums[i]
        if ans== 1000000000:
            return 0
        else:
            return ans