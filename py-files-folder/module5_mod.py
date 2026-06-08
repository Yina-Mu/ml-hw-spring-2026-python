# module5_mod.py

# This class stores numbers and searches for a target number.
class NumberCollection:
    def __init__(self):
        # Initialize an empty list to store the numbers.
        self.numbers = []

    def insert_number(self, number):
        # Add one number to the list.
        self.numbers.append(number)

    def search_number(self, target):
        # Search for the target number and return its 1-based index.
        for index, number in enumerate(self.numbers):
            if number == target:
                return index + 1

        # Return -1 if the target number is not found.
        return -1