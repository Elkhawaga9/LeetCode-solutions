class Solution:
    def findComplement(self, num: int) -> int:
        l = num.bit_length()
        return num^((1<<l)-1)

