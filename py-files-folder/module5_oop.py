# module5_oop.py

class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, target):
        for index, number in enumerate(self.numbers):
            if number == target:
                return index + 1
        return -1


def main():
    n = int(input("Please enter N: "))

    collection = NumberCollection()

    for i in range(n):
        number = int(input(f"Please enter number {i + 1}: "))
        collection.insert_number(number)

    x = int(input("Please enter X: "))

    result = collection.search_number(x)
    print(result)


if __name__ == "__main__":
    main()