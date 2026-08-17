from functools import cache

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0

            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for k in range(l, r):

                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                # Left side is smaller.
                if left_sum < right_sum:
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(l, k)
                    )

                elif left_sum > right_sum:
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, r)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + dfs(l, k),
                        right_sum + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)