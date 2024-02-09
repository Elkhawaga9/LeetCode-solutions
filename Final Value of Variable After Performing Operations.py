class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        answer = 0

        #update if condition satisfied
        for string in operations:
            if string=="X++" or string=="++X":
                answer+=1
            else:
                answer-=1

        return answer


        
