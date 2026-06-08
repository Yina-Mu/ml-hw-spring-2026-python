# module5_call.py

from module5_mod import NumberCollection


def main():
    # Read N, the number of values the user will enter.
    n = int(input("Please enter N: "))

    # Create an object of the NumberCollection class.
    collection = NumberCollection()

    # Read N numbers one by one and insert them into the collection.
    for i in range(n):
        number = int(input(f"Please enter number {i + 1}: "))
        collection.insert_number(number)

    # Read the target number X.
    x = int(input("Please enter X: "))

    # Search for X and print the result.
    result = collection.search_number(x)
    print(result)


if __name__ == "__main__":
    main()