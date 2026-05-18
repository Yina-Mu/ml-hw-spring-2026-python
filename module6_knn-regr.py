import numpy as np


class KNNRegression:
    def __init__(self):
        self.points = np.empty((0, 2), dtype=float)

    def insert_point(self, x, y):
        new_point = np.array([[x, y]], dtype=float)
        self.points = np.vstack((self.points, new_point))

    def predict(self, x_input, k):
        n = len(self.points)

        if k > n:
            raise ValueError("Error: k cannot be greater than N.")

        # Extract x values and y values
        x_values = self.points[:, 0]
        y_values = self.points[:, 1]

        # Calculate distances between input X and all training x values
        distances = np.abs(x_values - x_input)

        # Get indices of the k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # Get y values of the k nearest neighbors
        nearest_y_values = y_values[nearest_indices]

        # k-NN Regression result: average of nearest y values
        prediction = np.mean(nearest_y_values)

        return prediction


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def main():
    model = KNNRegression()

    N = read_positive_integer("Please enter N, the number of points: ")
    k = read_positive_integer("Please enter k, the number of nearest neighbors: ")

    print(f"Please enter {N} points one by one.")

    for i in range(N):
        print(f"Point {i + 1}:")
        x = read_real_number("Enter x value: ")
        y = read_real_number("Enter y value: ")
        model.insert_point(x, y)

    x_input = read_real_number("Please enter input X for prediction: ")

    try:
        result = model.predict(x_input, k)
        print(f"The predicted Y value using k-NN Regression is: {result}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()