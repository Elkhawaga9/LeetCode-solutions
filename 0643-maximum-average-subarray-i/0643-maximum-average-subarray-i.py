class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = sum(nums[:k])
        ans = w_sum/k
        for i in range(1,len(nums)-k+1):
            w_sum-=nums[i-1]
            w_sum+=nums[i+k-1]

            ans = max(ans,w_sum/k)
        return ans