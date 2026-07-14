class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        maximum_profit = 0
        for price in prices:
            current_profit = price - minimum_price
            maximum_profit = max(maximum_profit, current_profit)
            minimum_price = min(price, minimum_price)
        return maximum_profit
