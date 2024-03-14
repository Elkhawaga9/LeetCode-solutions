class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        p = len(nums)-1
        while k<p:
            nums[k], nums[p] = nums[p], nums[k]
            p-=1
            k+=1
        