class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # the slowest and the fastest k
        res = 0

        while l <= r:
            k = (r + l) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(p/k)     # total time
            if total_time > h:     # total time exceed given hours => find faster k
                l = k + 1
            elif total_time <= h:
                res = k
                r = k - 1   # attempt to find effective k
                
        return res

