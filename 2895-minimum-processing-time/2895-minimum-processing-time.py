class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        ans = 0
        j = 0
        for i in range(3,len(tasks),4):
            ans = max(ans,processorTime[j]+tasks[i])
            j+=1
        return ans