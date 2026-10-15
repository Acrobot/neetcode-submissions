from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        mid = 0
        while l < r:
            mid = l + (r - l) // 2

            s = sum(ceil(pile / mid) for pile in piles)
            if s <= h:
                r = mid
            else:
                l = mid + 1

        return l