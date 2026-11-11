class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, cost_both: int, need1: int, need2: int
    ) -> int:
        buy_individually = need1 * cost1 + need2 * cost2
        buy_only_bundles = cost_both * max(need1, need2)

        min_need = min(need1, need2)
        buy_mixed = (
            cost_both * min_need
            + (need1 - min_need) * cost1
            + (need2 - min_need) * cost2
        )

        return min(buy_individually, buy_only_bundles, buy_mixed)
