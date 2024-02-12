class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = 0
        ans = []
        for i in candies:
            max_num = max(max_num,i)
        
        for i in candies:
            if i+extraCandies>=max_num:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        
