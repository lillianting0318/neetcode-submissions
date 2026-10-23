class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_n, close_n):
            # end case
            if open_n == close_n == n:
                res.append("".join(stack))
                return
            # case 1: left parenthesis < n
            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, close_n)
                stack.pop()

            # case 2: right parenthesis < left
            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res