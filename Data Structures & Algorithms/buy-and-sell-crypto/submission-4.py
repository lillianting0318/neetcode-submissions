class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        l, r = 0, 1
        max_profit = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
                r += 1
            else:
                l = r
        r += 1
        return max_profit