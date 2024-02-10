class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        eq = []
        for i in nums:
            if i==pivot:
                eq.append(i)
            elif i>pivot:
                great.append(i)
            else:
                less.append(i)
        less.extend(eq)
        less.extend(great)
        return (less)   
