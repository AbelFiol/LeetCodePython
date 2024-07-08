from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # No need to modify for small arrays.

        k = 1  # Initialize the index for unique elements.
        for j in range(2, len(nums)):
            if nums[j] != nums[k - 1]:
                k += 1
                nums[k] = nums[j]

        return k + 1  # Return the final length of the modified array.