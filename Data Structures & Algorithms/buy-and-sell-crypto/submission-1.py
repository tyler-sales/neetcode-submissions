class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price <= curr_min:
                curr_min = price
            elif price - curr_min > max_profit:
                max_profit = price - curr_min
        return max_profit
        