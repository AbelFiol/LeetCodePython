from typing import List  # Importing List type from the typing module.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort the citations list in reverse order.
        h = 0  # Initialize the H-index to 0.
        for i, citation in enumerate(citations, start=1):  # Iterate through the sorted citations list.
            if citation >= i:  # Check if the current citation count is greater than or equal to its index.
                h = i  # Update the H-index if the condition is met.
        return h  # Return the calculated H-index.