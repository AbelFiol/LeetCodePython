from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize a pointer to keep track of the length of the result.
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the element to the front of the list.
                k += 1
        return k