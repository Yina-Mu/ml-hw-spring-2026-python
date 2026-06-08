import numpy as np
from sklearn.metrics import precision_score, recall_score


def main():
    number_of_points = int(input("Enter N, the total number of points: "))

    if number_of_points <= 0:
        print("N must be a positive integer here.")
        return

    # Initialize NumPy arrays
    ground_truth_labels = np.empty(number_of_points, dtype=int)
    predicted_labels = np.empty(number_of_points, dtype=int)

    # Read N pairs of labels
    for point_index in range(number_of_points):
        print(f"Enter point {point_index + 1}:")

        ground_truth_label = int(input("Enter x value, ground truth label, 0 or 1: "))
        predicted_label = int(input("Enter y value, predicted label, 0 or 1: "))

        if ground_truth_label not in [0, 1] or predicted_label not in [0, 1]:
            print("Both ground truth label and predicted label must be either 0 or 1.")
            return

        # Insert data into NumPy arrays
        ground_truth_labels[point_index] = ground_truth_label
        predicted_labels[point_index] = predicted_label

    # Compute Precision and Recall using Scikit-learn
    precision = precision_score(
        ground_truth_labels,
        predicted_labels,
        zero_division=0
    )

    recall = recall_score(
        ground_truth_labels,
        predicted_labels,
        zero_division=0
    )

    print("Precision:", precision)
    print("Recall:", recall)


if __name__ == "__main__":
    main()