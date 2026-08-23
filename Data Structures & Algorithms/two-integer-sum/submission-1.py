class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            prevMap[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap and prevMap[diff] != i:
                return [i, prevMap[diff]]
        return []