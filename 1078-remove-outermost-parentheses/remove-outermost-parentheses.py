class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0  
      
        for char in s:
            if char == '(':
                
                depth += 1
                if depth > 1:
                    result.append(char)
            else:
                depth -= 1

                if depth > 0:
                    result.append(char)
      
        return ''.join(result)
