class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        f = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                f = 1
            else:
                digits[i]+=1
                for i in range(i+1,len(digits)):
                    digits[i]=0
                f = 0
                break
        if f:
            digits = [0 for i in digits]
            digits.insert(0,1)
        return digits
