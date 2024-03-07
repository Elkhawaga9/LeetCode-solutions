class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
        ans = 0
        st = 0
        end = n-1
        while(st<=end):
            if people[st]+people[end]<=limit:
                st+=1
                end-=1
            else:
                end-=1
            ans+=1
        return ans  