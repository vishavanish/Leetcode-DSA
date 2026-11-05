from typing import List
from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()

        # Initialize counter for valid elements
        distance_value_count = 0

        # Check each element in arr1
        for num in arr1:
            left_bound_index = bisect_left(arr2, num - d)

            # An element from arr1 is valid if:
            is_valid = (left_bound_index == len(arr2) or arr2[left_bound_index] > num + d)
            distance_value_count += is_valid

        return distance_value_count
