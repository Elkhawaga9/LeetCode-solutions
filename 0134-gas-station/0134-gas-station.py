class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        diff: -2 -2 -2 3 3
        diff: -1 -1 1
        """
        if sum(gas)<sum(cost):
            return -1
        alltank = 0
        pos = 0 
        for i in range(len(gas)):
            if alltank + gas[i]-cost[i]<0:
                alltank = 0
                pos = i+1
            else:
                alltank+=gas[i]-cost[i]
        return pos

