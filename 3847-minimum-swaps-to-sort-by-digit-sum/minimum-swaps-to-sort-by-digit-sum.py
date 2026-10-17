class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def calculate_digit_sum(number: int) -> int:
            digit_sum = 0
            while number:
                digit_sum += number % 10
                number //= 10
            return digit_sum

        n = len(nums)
        sorted_pairs = sorted((calculate_digit_sum(num), num) for num in nums)
    
        value_to_target_position = {pair[1]: index for index, pair in enumerate(sorted_pairs)}
      
        min_swaps_needed = n
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                min_swaps_needed -= 1
                current_position = i
                while not visited[current_position]:
                    visited[current_position] = True
                    current_position = value_to_target_position[nums[current_position]]
      
        return min_swaps_needed
