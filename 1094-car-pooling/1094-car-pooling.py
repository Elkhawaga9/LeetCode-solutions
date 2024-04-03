class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        positions = [0]*(1002)
        for p,f,to in trips:
            positions[f]+=p
            positions[to]-=p
        for i in range(1,1002):
            positions[i]+=positions[i-1]
            if positions[i]>capacity:
                return False
        return True
        

        