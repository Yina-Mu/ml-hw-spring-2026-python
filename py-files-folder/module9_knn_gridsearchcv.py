import numpy as np
from sklearn.model_selection import GridSearchCV, StratifiedKFold, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def read_dataset(dataset_name, size):
    x_values = np.empty((size, 1), dtype=float)
    y_values = np.empty(size, dtype=int)

    print(f"\nEnter {size} (x, y) pairs for {dataset_name}:")

    for i in range(size):
        x = read_real_number(f"{dataset_name} pair {i + 1} - x value: ")
        y = read_non_negative_integer(f"{dataset_name} pair {i + 1} - y value: ")

        x_values[i, 0] = x
        y_values[i] = y

    return x_values, y_values


def choose_cv_strategy(y_train):
    n_samples = len(y_train)

    if n_samples < 2:
        return None

    unique_classes, class_counts = np.unique(y_train, return_counts=True)
    min_class_count = np.min(class_counts)

    if len(unique_classes) >= 2 and min_class_count >= 2:
        n_splits = min(5, min_class_count)
        return StratifiedKFold(
            n_splits=n_splits,
            shuffle=True,
            random_state=42
        )

    n_splits = min(5, n_samples)

    if n_splits >= 2:
        return KFold(
            n_splits=n_splits,
            shuffle=True,
            random_state=42
        )

    return None


def get_valid_k_values(n_train, cv, y_train):
    if cv is None:
        return [1]

    min_training_fold_size = n_train
    dummy_x = np.zeros((n_train, 1))

    for train_index, _ in cv.split(dummy_x, y_train):
        min_training_fold_size = min(min_training_fold_size, len(train_index))

    max_k = min(10, min_training_fold_size)

    return list(range(1, max_k + 1))


def main():
    print("KNN Classification with GridSearchCV")

    n = read_positive_integer("\nEnter N, the number of training pairs: ")
    x_train, y_train = read_dataset("training set", n)

    m = read_positive_integer("\nEnter M, the number of test pairs: ")
    x_test, y_test = read_dataset("test set", m)

    knn = KNeighborsClassifier()

    cv = choose_cv_strategy(y_train)
    valid_k_values = get_valid_k_values(len(y_train), cv, y_train)

    param_grid = {
        "n_neighbors": valid_k_values
    }

    if cv is None:
        best_k = 1
        best_model = KNeighborsClassifier(n_neighbors=best_k)
        best_model.fit(x_train, y_train)
    else:
        grid_search = GridSearchCV(
            estimator=knn,
            param_grid=param_grid,
            scoring="accuracy",
            cv=cv
        )

        grid_search.fit(x_train, y_train)

        best_k = grid_search.best_params_["n_neighbors"]
        best_model = grid_search.best_estimator_

    y_pred = best_model.predict(x_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    print("\nResult:")
    print(f"Best k: {best_k}")
    print(f"Test accuracy: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()