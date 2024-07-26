from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize a variable to keep track of the furthest position you can reach.
        max_reachable = 0
        
        # Iterate through the array.
        for i in range(len(nums)):
            # If the current index is beyond the furthest position you can reach, return False.
            if i > max_reachable:
                return False
            
            # Update the furthest position you can reach.
            max_reachable = max(max_reachable, i + nums[i])
            
            # If you can reach the last index, return True.
            if max_reachable >= len(nums) - 1:
                return True
        
        return False  # If the loop completes without reaching the last index, return False.