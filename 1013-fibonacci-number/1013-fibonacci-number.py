sav = dict()

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        if n in sav:
            return sav[n]
        else: 
            sav[n] = self.fib(n-1)+self.fib(n-2)
            return sav[n] 