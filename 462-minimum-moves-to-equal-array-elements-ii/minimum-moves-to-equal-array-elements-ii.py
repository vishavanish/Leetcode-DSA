class Solution:
    def minMoves2(self, nums):

        sorted_nums = sorted(nums)  # Creates a new sorted list
        median = sorted_nums[len(sorted_nums) >> 1]

        return sum(abs(v - median) for v in nums)
        