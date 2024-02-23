
class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
       n = len(nums)
       suff = [0 for _ in range(n)]
       pref = [0 for _ in range(n)]
       suff[n-1] = int(nums[n-1]==1)
       if nums[0]==0:
           pref[0]=1
       for i in range(1,len(nums)):
           pref[i] = pref[i-1]+int(nums[i]==0)

       for i in range(len(nums)-2,-1,-1):
           suff[i] = suff[i + 1] + int(nums[i]==1)

       ans =[]
       mx = pref[n-1]
       ans.append(n)
       if suff[0]==mx:
           ans.append(0)
       elif suff[0]>mx:
           ans.clear()
           ans.append(0)
           mx = suff[0]
       for i in range(n-1):

           if pref[i]+suff[i+1]>mx:
               ans.clear()
               ans.append(i+1)
               mx = pref[i]+suff[i+1]
           elif pref[i]+suff[i+1]==mx:
               ans.append(i+1)

       return ans
