class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for a,b in costs:
            diff.append([b-a,a,b])
        diff.sort() # the less difference means we should take the b 
        ans = 0
        for i in range(len(costs)):
            if i<len(diff)//2:
                ans+=diff[i][2]
            else:
                ans+=diff[i][1]
        return ans

            

        