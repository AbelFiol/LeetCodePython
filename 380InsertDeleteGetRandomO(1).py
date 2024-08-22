import random

class RandomizedSet:

    def __init__(self):
        # Initialize an empty list to store elements.
        self.array = []
        # Initialize an empty dictionary to store the mapping of elements to their indices.
        self.index_map = {}        

    def insert(self, val: int) -> bool:
        # Check if the value already exists in the set.
        if val in self.index_map:
            # If value exists, return False (insertion failed).
            return False

        # Append the value to the end of the list.
        self.array.append(val)
        # Update the index map with the index of the newly inserted value.
        self.index_map[val] = len(self.array) - 1

        # Return True to indicate successful insertion.
        return True

    def remove(self, val: int) -> bool:
        # Check if the value exists in the set.
        if val not in self.index_map:
            # If value doesn't exist, return False (removal failed).
            return False

        # Get the index of the value from the index map.
        index = self.index_map[val]
        # Get the length of the array.
        array_length = len(self.array)

        # If the value is not the last element in the array.
        if index != array_length - 1:
            # Swap the value with the last element in the array.
            self.array[array_length - 1], self.array[index] = self.array[index], self.array[array_length - 1]
            # Update the index of the last element in the index map.
            self.index_map[self.array[index]] = index

        # Remove the last element from the array.
        self.array.pop()
        # Remove the value from the index map.
        del self.index_map[val]

        # Return True to indicate successful removal.
        return True

    def getRandom(self) -> int:
        # Generate a random index within the range of the array length.
        index = int(random.random() * len(self.array))
        # Return the element at the random index.
        return self.array[index]