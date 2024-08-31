class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        allXor = 0
        for num in nums:
            allXor^=num
        #print(allXor)
        st = bin(allXor)
        
        diff = 0
        for i in range(len(st)-1,-1,-1):
            if st[i]=='1':
                diff = len(st)-i-1
                break

        first = 0
        second = 0

        mask = 1<<diff
        print(mask)
        for num in nums:
            if mask&num:
                first^=num
            else:
                second^=num
        return [first,second]

        