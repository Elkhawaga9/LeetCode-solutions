class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def found(arr):
            low=0
            high=len(row)-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==target:
                    return True
                elif  arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1  
            return False          
        for row in matrix:
            if found(row):
                return True

        return False        

        