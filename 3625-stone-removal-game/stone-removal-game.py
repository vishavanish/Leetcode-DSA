class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        # Start with removing 10 stones in the first turn
        stones_to_remove = 10
      
        # Count the total number of turns played
        total_turns = 0
      
        # Continue playing while there are enough stones to remove
        while n >= stones_to_remove:
            # Remove stones from the pile
            n -= stones_to_remove
          
            # Next turn requires removing one less stone
            stones_to_remove -= 1
          
            # Increment turn counter
            total_turns += 1
      
        # Alice wins if the total number of turns is odd
        # (Alice plays on odd turns: 1st, 3rd, 5th, etc.)
        return total_turns % 2 == 1
