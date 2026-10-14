class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = [0] * len(prices)

        for idx, price in enumerate(prices[::-1]):
            max_prices[len(prices)-1-idx] = \
                max(max_prices[len(prices)-idx], price) \
                if idx != 0 else price

        best_profit = 0

        for idx, price in enumerate(prices):
            best_profit = max(max_prices[idx] - price, best_profit)

        return best_profit
        