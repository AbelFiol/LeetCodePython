from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables for buying index and maximum profit.
        buy = 0
        max_profit = 0
        
        # Iterate through the prices list to find the maximum profit.
        for i in range(len(prices)):
            # If the current price is lower than the price at the buying index, update the buying index.
            if prices[i] < prices[buy]:
                buy = i
            # If the profit by selling at the current price is higher than the recorded maximum profit, update it.
            elif prices[i] - prices[buy] > max_profit:
                max_profit = prices[i] - prices[buy]
        
        return max_profit  # Return the maximum profit obtained.