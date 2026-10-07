class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(index: int, left_to_remove: int, right_to_remove: int, 
                left_count: int, right_count: int, current_string: str) -> None:
            """
            Recursively explore all possible ways to remove invalid parentheses.
          
            Args:
                index: Current position in the original string
                left_to_remove: Number of '(' that still need to be removed
                right_to_remove: Number of ')' that still need to be removed
                left_count: Count of '(' in the current valid string being built
                right_count: Count of ')' in the current valid string being built
                current_string: The string being constructed
            """
            # Base case: reached end of string
            if index == string_length:
                if left_to_remove == 0 and right_to_remove == 0:
                    valid_results.add(current_string)
                return
          
            if string_length - index < left_to_remove + right_to_remove or left_count < right_count:
                return
          
            if s[index] == '(' and left_to_remove > 0:
                dfs(index + 1, left_to_remove - 1, right_to_remove, 
                    left_count, right_count, current_string)
          
            elif s[index] == ')' and right_to_remove > 0:
                dfs(index + 1, left_to_remove, right_to_remove - 1, 
                    left_count, right_count, current_string)
          
            new_left_count = left_count + (1 if s[index] == '(' else 0)
            new_right_count = right_count + (1 if s[index] == ')' else 0)
            dfs(index + 1, left_to_remove, right_to_remove, 
                new_left_count, new_right_count, current_string + s[index])
      
        left_to_remove = 0
        right_to_remove = 0
      
        for char in s:
            if char == '(':
                left_to_remove += 1
            elif char == ')':
                if left_to_remove > 0:
                    left_to_remove -= 1
                else:
                    right_to_remove += 1
      
        valid_results = set()
        string_length = len(s)
      
        dfs(0, left_to_remove, right_to_remove, 0, 0, '')
      
        return list(valid_results)
