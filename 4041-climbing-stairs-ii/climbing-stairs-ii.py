class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        num_stairs = len(costs)

        dp = [inf] * (num_stairs + 1)
        dp[0] = 0

        for i, cost in enumerate(costs, 1):
            for j in range(i - 3, i):
                if j >= 0:
                    dp[i] = min(dp[i], dp[j] + cost + (i - j) ** 2)

        # The answer is the minimum cost to reach the top stair
        return dp[num_stairs]
