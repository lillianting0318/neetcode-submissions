class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        # Sort the array so duplicates appear next to each other
        candidates.sort()
        
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            # choose candidates[i]
            subset.append(candidates[i])
            # i + 1 because every number only use once
            dfs(i + 1, total + candidates[i])

            # backtracking
            subset.pop()

            # not to choose candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)
        return res
            



