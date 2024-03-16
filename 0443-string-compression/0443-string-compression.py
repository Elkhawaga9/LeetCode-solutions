class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        ans = [chars[0]]
        tmp = 1
        for i in range(1, n):
            if chars[i] == chars[i - 1]:
                tmp += 1
            else:
                if tmp > 1:
                    ans.extend(list(str(tmp)))
                ans.append(chars[i])
                tmp = 1  
        if tmp > 1:  
            ans.extend(list(str(tmp)))
        chars[:] = ans 
        return len(ans)
