class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = high = profit = 0
        while high < len(prices):
            profit = max(profit,prices[high] - prices[low])
            while prices[high] - prices[low] < 0:
                low += 1
            high += 1
        return profit