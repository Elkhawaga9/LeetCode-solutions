from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        unique = defaultdict(int)
        left = 0
        ret = 0
        for right in range(len(fruits)):
            unique[fruits[right]]+=1
            while(len(unique)>2):
                unique[fruits[left]]-=1
                if unique[fruits[left]]==0:
                    del unique[fruits[left]]
                left += 1
            ret = max(ret,right-left+1)
        return ret
