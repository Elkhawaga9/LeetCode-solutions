class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations ="+-*/"
        for ch in tokens:
            if ch in operations:
                p1 = stack.pop()
                p2 = stack.pop()
                if ch=='+':
                    stack.append(p2+p1)
                elif ch=='-':
                    stack.append(p2-p1)
                elif ch=='*':
                    stack.append(p2*p1)
                elif ch=='/':
                    stack.append(int(p2/p1))
            else:
                stack.append(int(ch))
            
            #print(stack)
        return stack[0] 
        