class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        ans = []
        n = len(firstList)
        m = len(secondList)
        l = 0
        r= 0
        while (l<n and r<m):
            s1,e1 = firstList[l]
            s2,e2 = secondList[r]
            if (s1<=e2 and e1>=s2):
                ans.append([max(s1,s2),min(e1,e2)])
            if (e2>e1):
                l+=1
            else:
                r+=1
        return ans