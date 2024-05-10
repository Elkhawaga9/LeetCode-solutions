class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        small = -1
        great = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                small = mid
                r = mid - 1  
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if small==-1:
            return[-1,-1]

        l = small
        r = n-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                great = mid
                l = mid+1
            else:
                r = mid-1
        return [small,great]

        