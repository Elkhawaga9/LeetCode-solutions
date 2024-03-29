from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0

        # 0 5
        if n==1:
            if nums[0]%k==0:
                return 1
            else:
                return 0
                

        for i in range(1,n):
            nums[i]+=nums[i-1]
        for i in nums:
            freq[i%k]+=1
        for i,j in freq.items():
            search_for = i%k
            ans+=freq[search_for]
            freq[search_for]+=1

        return ans