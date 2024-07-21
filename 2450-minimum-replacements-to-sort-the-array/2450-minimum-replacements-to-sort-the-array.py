class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        3 10 3 
        3    3 
        3 
        """
        nxt = nums[-1]
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nxt:
                parts = ceil(nums[i]/nxt) 
                ans+=parts-1 
                nxt = nums[i]//parts # 10//4 -> 3.3333    ->   2 2 3 3
            else:
                nxt = nums[i]
        return ans

                 

          