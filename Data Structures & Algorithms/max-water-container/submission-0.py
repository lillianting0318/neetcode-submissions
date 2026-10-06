class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        n = len(heights)
        l, r = 0, n - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maxA = max(maxA, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA
