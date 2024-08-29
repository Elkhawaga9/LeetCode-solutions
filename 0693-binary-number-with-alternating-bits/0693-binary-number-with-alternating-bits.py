class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for i in range(1,len(n)):
            if not (int(n[i])^int(n[i-1])):
                return False
        return True


        