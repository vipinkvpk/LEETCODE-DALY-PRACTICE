class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price=prices[0]
        max_profit=0

        for i in range(1, len(prices)):
            current_price = prices[i]
            max_profit = max(max_profit, current_price - min_price)
            min_price= min(min_price, current_price)
        return max_profit