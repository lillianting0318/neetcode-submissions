class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()    # add all visited nodes in the past to make sure don't revisit it
        
        def dfs(r, c, i):
            # base case (every chars in the word are match)
            if i == len(word):
                return True
            # if out of space, char doesn't match, the position is already in set()
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # path occupied (r, c)
            path.add((r,c))
            # try four ways
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            # unoccupied (r, c)
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False