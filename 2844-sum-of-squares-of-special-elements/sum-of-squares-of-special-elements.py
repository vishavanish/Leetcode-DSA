class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)
      
        result = sum(
            num * num
            for index, num in enumerate(nums, 1)
            if n % index == 0 
        )
      
        return result
