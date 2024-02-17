class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        tot = capacity
        ans = 0
        for i in range(len(plants)):
            if capacity>=plants[i]:
                ans+=1
                capacity-=plants[i]
            else:
                ans += i
                ans+=i+1
                capacity = tot-plants[i]

        return (ans)

        
