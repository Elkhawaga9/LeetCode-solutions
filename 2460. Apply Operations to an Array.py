class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        ans = []
        c =0
        print(nums)
        for i in nums:
            if i == 0:
                c+=1
            else:
                ans.append(i)
        while(c):
            ans.append(0)
            c-=1
        return (ans)
