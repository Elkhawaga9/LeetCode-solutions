class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        valid = set()
        non_valid = set()
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                valid.add(fronts[i])
                valid.add(backs[i])
            else:
                non_valid.add(fronts[i])
        if len(valid) == 0:
            return 0

        ans = 99999999
        for i in valid:
            if i not in non_valid:
                ans = min(ans,i)
        return ans%99999999


        
