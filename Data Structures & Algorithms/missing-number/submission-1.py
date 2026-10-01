class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res