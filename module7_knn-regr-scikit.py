import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_positive_integer(prompt):
    """Read and validate a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid positive integer.")


            return float(input(prompt))
    X_train = np.empty((N, 1), dtype=float)
        # Data insertion using NumPy arrays
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegressorApp:
    def __init__(self):
        self.N = 0
        self.k = 0
        self.X_train = None
        self.y_train = None
        self.query_x = 0.0
        self.model = None

    def read_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Error: Please enter a positive integer.")
                    continue
                return value
            except ValueError:
                print("Error: Please enter a valid positive integer.")

    def read_real_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a valid real number.")

    def input_data(self):
        self.N = self.read_positive_integer("Enter N (positive integer): ")
        self.k = self.read_positive_integer("Enter k (positive integer): ")
        self.X_train = np.empty((self.N, 1), dtype=float)
        self.y_train = np.empty(self.N, dtype=float)
        print(f"Please enter {self.N} (x, y) points.")
        for i in range(self.N):
            x_value = self.read_real_number(f"Enter x value for point {i + 1}: ")
            y_value = self.read_real_number(f"Enter y value for point {i + 1}: ")
            self.X_train[i, 0] = x_value
            self.y_train[i] = y_value
        self.query_x = self.read_real_number("Enter X value for prediction: ")

    def validate_k(self):
        if self.k > self.N:
            print(f"Error: k must be less than or equal to N. You entered k={self.k}, N={self.N}.")
            return False
        return True

    def train_and_predict(self):
        label_variance = np.var(self.y_train)
        self.model = KNeighborsRegressor(n_neighbors=self.k)
        self.model.fit(self.X_train, self.y_train)
        query_point = np.array([[self.query_x]], dtype=float)
        predicted_y = self.model.predict(query_point)[0]
        print(f"Predicted Y using k-NN Regression: {predicted_y}")
        print(f"Variance of labels in the training dataset: {label_variance}")

    def run(self):
        self.input_data()
        if self.validate_k():
            self.train_and_predict()


if __name__ == "__main__":
    app = KNNRegressorApp()
    app.run()