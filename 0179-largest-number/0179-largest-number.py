class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        def comp(x1,x2):
            if x1+x2>=x2+x1:
                return 1
            else:
                return -1
        nums = sorted([str(i) for i in nums],reverse = True,key=cmp_to_key(comp))
        return ''.join(nums)
        """
        9 5 34 31 30 3
        9 5 43 13 03 30
        """

