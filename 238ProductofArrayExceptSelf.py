from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a list to store the final result, initially filled with 1s.
        result = [1] * len(nums)

        # Define a helper function to calculate the product.
        def calculate_product(iterator):
            running_product = 1
            # Iterate through the indices specified by the iterator.
            for i in iterator:
                # Update the result at index i by multiplying it with the running product.
                result[i] *= running_product
                # Update the running product by multiplying it with the corresponding number in nums.
                running_product *= nums[i]

        # Calculate the product of all elements before each index.
        calculate_product(range(len(nums)))   
        # Calculate the product of all elements after each index.
        calculate_product(range(len(nums)-1, -1, -1))
        
        # Return the final result.
        return result