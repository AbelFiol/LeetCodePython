from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if the total amount of gas available is less than the total cost of the journey.
        if sum(gas) < sum(cost):
            return - 1  # Cannot complete the circuit, return - 1.
        
        total_gas = 0  # Initialize total gas available.
        start_station = 0  # Initialize the start station index.
        
        # Iterate over each gas station.
        for i in range(len(gas)):
            # Update total_gas by adding gas at the current station and subtracting the cost to travel to the next station.
            total_gas += (gas[i] - cost[i])
            
            # If total_gas becomes negative, reset total_gas to 0 and update the start_station to the next station.
            if total_gas < 0:
                total_gas = 0
                start_station = i + 1
        
        return start_station  # Return the index of the starting gas station from where the circuit can be completed.