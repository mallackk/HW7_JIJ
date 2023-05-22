import numpy as np


def main():
    # Compute the eigenvalues, eigenvectors, and the determinant of a given square array
    arr = np.array([[1, 2], [3, 4]])
    w, v = np.linalg.eig(arr)

    print(f"Eigenvalues: {w}")
    print(f"Eigenvectors: ", end="")
    for tmp in v:
        print(f"{tmp}, ", end="")
    print()

    adet = np.linalg.det(arr)
    print(f"Determinant: {adet}")

    # Calculate the cross product of two given vectors
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])

    vec = np.cross(vec1, vec2)
    print(f"Cross product: {vec}")

    # Solve the following system of linear equations.
    A = np.array([[1, 2, -2], [2, 1, -5], [1, -4, 1]])
    b = np.array([-15, -21, 18])
    x = np.linalg.solve(A, b)
    print(f"Solution: {x}")


if __name__ == "__main__":
    main()
