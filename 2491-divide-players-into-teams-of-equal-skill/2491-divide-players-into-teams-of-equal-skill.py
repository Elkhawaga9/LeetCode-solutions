class Solution:
   def dividePlayers(self, skill: list[int]) -> int:
      skill.sort()
      st = 0
      end = len(skill)-1
      ans = 0
      g = skill[st]+skill[end]
      while(st<=end):
         if skill[st]+skill[end]==g:
            ans+=skill[st]*skill[end]
            st+=1
            end-=1
         else:
            return -1
      return ans
            

            
        