class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
      
        parity_count = [1, 0]
      
        # Total count of subarrays with odd sum
        result = 0
      
        # Running prefix sum
        prefix_sum = 0
      
        for num in arr:
            # Update prefix sum
            prefix_sum += num
          
            # Get current parity (0 for even, 1 for odd)
            current_parity = prefix_sum & 1
          
            opposite_parity = current_parity ^ 1
          
            # Add count of prefix sums with opposite parity
            result = (result + parity_count[opposite_parity]) % MOD
          
            # Update count for current parity
            parity_count[current_parity] += 1
      
        return result
