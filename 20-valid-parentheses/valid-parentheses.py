class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []

        # Set of valid bracket pairs
        valid_pairs = {'()', '[]', '{}'}

        # Iterate through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If it's a closing bracket
            else:
                # Check if stack is empty (no matching opening bracket)
                # or if the top opening bracket doesn't match with current closing bracket
                if not stack or stack[-1] + char not in valid_pairs:
                    return False

                # Valid matching pair found, remove the opening bracket from stack
                stack.pop()

        # All brackets are valid if stack is empty (all opening brackets were matched)
        return not stack
