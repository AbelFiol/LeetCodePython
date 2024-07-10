from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each element.
        count_dict = {}

        # Iterate through the array.
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        
        # Find the element with the maximum count.
        majority_element = max(count_dict, key=count_dict.get)

        return majority_element