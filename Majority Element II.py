from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        print(nums)
        ans = set()
        for x,y in nums.items():
            if y > n/3:
                ans.add(x)
        ans = list(ans)
        return (ans)

        
