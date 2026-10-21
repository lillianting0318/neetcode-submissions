class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            # end condition
            if total == target:
                res.append(subset.copy())
                return

            # Pruning
            if total > target or i >= len(nums):
                return

            # decision to choose nums[i]
            subset.append(nums[i])
            # dfs still return i because can nums can be chosen unlimited times
            dfs(i, total + nums[i])
            
            # backtracking
            subset.pop()

            # decision not to choose nums[i]
            dfs(i + 1, total)
        dfs(0, 0)
        return res

            

