class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')': '(', '}': '{', ']': '['}

        for c in s:
            # c is ')}]'
            if c in valid:
                # stack[-1] is '({['
                if stack and stack[-1] == valid[c]:
                    stack.pop()
                else:
                    return False
            # c is '({['
            else:
                stack.append(c)

        # if stack is empty
        if not stack:
            return True
        else: 
            return False