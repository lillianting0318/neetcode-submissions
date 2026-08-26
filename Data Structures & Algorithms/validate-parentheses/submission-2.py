class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ']':'[', ')':'('}
        
        for c in s:
            # check if c is one of the keys: }, ], )
            if c in closeToOpen:
                # check if stack is non-empty and the toppest element is the match value of c
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            # c is {, [, ( 
            else:
                stack.append(c)

        return True if not stack else False