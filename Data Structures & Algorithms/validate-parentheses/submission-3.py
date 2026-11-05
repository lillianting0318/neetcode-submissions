class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_parentheses = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in match_parentheses:
                if stack and stack[-1] == match_parentheses[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False