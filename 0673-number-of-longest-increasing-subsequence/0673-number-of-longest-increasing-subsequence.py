class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1]*(n)
        count = [1]*(n)

        """
                1 3 5 4 7
        length  1 2 3 3 4
        count   1 1 1 1 2
        """

        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if length[i] < length[j]+1:
                        length[i] = length[j]+1
                        count[i] = count[j]
                    elif length[i] == length[j]+1:
                        count[i] += count[j]
        print(length,count)
        max_len = max(length)
        ans = 0
        for i in range(n):
            if length[i]==max_len:
                ans+=count[i]
        return ans         
