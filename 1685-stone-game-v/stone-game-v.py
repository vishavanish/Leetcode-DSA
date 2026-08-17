from functools import cache

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sum
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

                    # Even if we could get left_sum again,
                    # maximum possible = 2 * left_sum.
                    #
                    # If that cannot beat ans, skip this split.
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(l, k)
                    )

                # Right side is smaller.
                elif left_sum > right_sum:

                    # As k moves right:
                    # left_sum increases
                    # right_sum decreases
                    #
                    # So future right_sum will only become smaller.
                    #
                    # If even 2 * right_sum can't beat ans,
                    # we can stop completely.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, r)
                    )

                # Equal
                else:
                    ans = max(
                        ans,
                        left_sum + dfs(l, k),
                        right_sum + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)