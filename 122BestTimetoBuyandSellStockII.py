from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        # Iterate through prices and calculate the profit by buying and selling on the same day.
        for i in range(1, len(prices)):
            # If the price difference is positive, add it to the total profit.
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit