class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
       ans = 0
       tempProduct = 1
       n = len(nums)
       p = 0
       lsub = 0
       for i in range(n):
            while p<n and tempProduct*nums[p]<k:
                lsub+=1
                tempProduct*=nums[p]
                p+=1
            ans+=lsub
            lsub-=1
            tempProduct/=nums[i]
       if ans<0:
           return 0
       else:
           return ans  