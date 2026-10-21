class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path: List[int]):
            # end condition
            if len(path) == len(nums):
                res.append(path[:])
                return

            # iterate every nums
            for i in range(len(nums)):
                # if the num has been used, skip it
                if used[i]:
                    continue

                # Choose used[i]
                used[i] = True
                path.append(nums[i])

                # iteration
                backtrack(path)

                # backtracking
                path.pop()
                used[i] = False

        backtrack([])
        return res