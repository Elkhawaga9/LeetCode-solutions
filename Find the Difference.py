class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        list_of_frequencies = [0 for i in range(26)]
        answer = ""
        #update the frequency of each element in s
        for char in s:
            list_of_frequencies[ord(char)-ord('a')]+=1

        for char in t:
            list_of_frequencies[ord(char)-ord('a')]-=1
            if list_of_frequencies[ord(char)-ord('a')]<0:
                answer+=char
        return answer


        
        
