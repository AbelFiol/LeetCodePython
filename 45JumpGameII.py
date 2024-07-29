from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  # If there is only one element, no need to jump.
            return 0

        jumps = 1  # Initialize jumps to 1 because we are considering the first jump from index 0.
        maxJumpIndex = nums[0]  # Represents the maximum index that can be reached with the current number of jumps.
        farthest = nums[0]  # Represents the farthest index that can be reached after taking the current jump.

        for i in range(1, n):
            if i > maxJumpIndex:  # If the current index is beyond the reach of current jumps, take another jump.
                jumps += 1
                maxJumpIndex = farthest
            farthest = max(farthest, i + nums[i])  # Update farthest reachable index.

        return jumps