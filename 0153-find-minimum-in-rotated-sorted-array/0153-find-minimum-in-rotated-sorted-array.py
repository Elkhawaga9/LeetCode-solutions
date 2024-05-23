class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        ans = -1
        while (l <= r):
            mid = (l + r) // 2
            if nums[l]>= nums[mid] <= nums[r]:
                r = mid
                ans = nums[mid]
            elif nums[l] < nums[mid] >nums[r]:
                l = mid+1
            elif nums[l]<nums[mid]<nums[r]:
                ans = nums[l]
                r = mid
            else:
                l = mid+1
            if l==r:
                return nums[l]
        return ans
