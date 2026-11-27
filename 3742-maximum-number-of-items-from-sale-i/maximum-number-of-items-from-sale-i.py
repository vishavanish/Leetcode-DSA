from typing import List
from math import inf


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0] * (budget + 1)
        min_price = inf

        for factor, price in items:
            # update the cheapest price seen so far
            min_price = min(min_price, price)

            # value of taking this item = number of items whose factor is
            # divisible by the current item's factor
            value = sum(other_factor % factor == 0 for other_factor, _ in items)
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + value)

        return max(
            value + (budget - i) // min_price
            for i, value in enumerate(dp)
        )
