N = int(input("Enter N: "))

numbers = []

for i in range(N):
    num = int(input("Enter a number: "))
    numbers.append(num)

X = int(input("Enter X: "))

found_index = -1

for i in range(N):
    if numbers[i] == X:
        found_index = i + 1
        break

print(found_index)