class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        for l1 in matches:
            if l1[1] in dict1:
                dict1[l1[1]] += 1
            else:
                dict1[l1[1]] = 1

        ans = [[], []]

        for k,v in dict1.items():
            if v==0:
                ans[0].append(k)
            elif v==1:
                ans[1].append(k)

        for l1 in matches:
            if l1[0] not in dict1:
                ans[0].append(l1[0])
                dict1[l1[0]]=0

        ans[0].sort()
        ans[1].sort()
        return ans
            
