from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to keep track of the index for non-val elements.

        # Iterate through each element in the nums list.
        for i in range(len(nums)):
            # If the current element is not equal to the value to remove.
            if nums[i] != val:
                nums[k] = nums[i]  # Place the element at the next position of k.
                k += 1  # Move the pointer k to the right.

        return k  # Return the new length of the modified list.