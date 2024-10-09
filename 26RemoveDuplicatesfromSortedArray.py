from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0  # Pointer for the index of unique elements.

        for i in range(1, len(nums)):  # Start from the second element.
            if nums[i] != nums[j]:  # Check if the current element is different from the last unique element.
                j += 1  # Move the pointer for unique elements forward.
                nums[j] = nums[i]  # Update the next unique position with the current element.

        return j + 1  # Return the count of unique elements.