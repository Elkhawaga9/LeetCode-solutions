class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            if i == ')' and stack[-1]=='(':
                stack.pop()
            elif i == '}' and stack[-1]=='{':
                stack.pop()
            elif i == ']' and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True




        