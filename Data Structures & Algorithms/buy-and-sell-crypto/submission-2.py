class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_up_to_now: int | None = None
        best_diff = 0

        for price in prices:
            if min_up_to_now is None or min_up_to_now > price:
                min_up_to_now = price
            
            best_diff = max(best_diff, price - min_up_to_now)

        return best_diff
        