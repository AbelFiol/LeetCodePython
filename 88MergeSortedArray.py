from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1  # Set pointers for nums1, nums2, and the last position in nums1.

        while j >= 0:  # Continue until all elements in nums2 are processed.
            if i >= 0 and nums1[i] > nums2[j]:  # If nums1 has elements left and nums1[i] is larger, copy it.
                nums1[k] = nums1[i]
                i -= 1  # Move the pointer for nums1 to the left.
            else:
                nums1[k] = nums2[j]  # Otherwise, copy nums2[j] into nums1.
                j -= 1  # Move the pointer for nums2 to the left.
            k -= 1  # Move the merge pointer to the left.