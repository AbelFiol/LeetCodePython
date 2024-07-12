from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Ensure k is within the range of array length to avoid redundant rotations.
        k = k % len(nums)
        
        # Rotate the array by assigning the sliced array with shifted elements.
        nums[:] = nums[-k:] + nums[:-k]  # Combining the elements after rotation.