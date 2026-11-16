class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            segment_sums = []
            string_length = len(s)
          
            for start_index in range(0, string_length, k):
                segment_sum = 0
              
                for index in range(start_index, min(start_index + k, string_length)):
                    segment_sum += int(s[index])
              
                segment_sums.append(str(segment_sum))
          
            s = "".join(segment_sums)
      
        return s
