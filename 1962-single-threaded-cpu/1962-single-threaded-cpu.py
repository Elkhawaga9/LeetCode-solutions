from heapq import heappush, heappop
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        if n == 0:
            return []

        for i in range(n):
            tasks[i].append(i)

        tasks.sort(key=lambda x: x[0])

        result = []
        min_heap = []
        current_time = tasks[0][0]
        index = 0
        
        while min_heap or index < n:
            while index < n and tasks[index][0] <= current_time:
                heappush(min_heap, (tasks[index][1], tasks[index][2]))
                index += 1
            
            if min_heap:
                duration, task_index = heappop(min_heap)
                current_time += duration
                result.append(task_index)
            else:
                if index < n:
                    current_time = tasks[index][0]
        
        return result
