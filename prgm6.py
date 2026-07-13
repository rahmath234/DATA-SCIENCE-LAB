import numpy as np

# 1. Get dimensions and elements for Matrix A
r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter columns for Matrix A: "))
print(f"Enter {r1} rows (numbers separated by spaces):")
A = np.array([[float(x) for x in input(f"Row {i+1}: ").split()] for i in range(r1)])

# 2. Get dimensions and elements for Matrix B
r2 = int(input("\nEnter rows for Matrix B: "))
c2 = int(input("Enter columns for Matrix B: "))
print(f"Enter {r2} rows (numbers separated by spaces):")
B = np.array([[float(x) for x in input(f"Row {i+1}: ").split()] for i in range(r2)])

# Display matrices
print(f"\nMatrix A:\n{A}\n")
print(f"Matrix B:\n{B}\n")

# 3. Matrix Addition
if A.shape == B.shape:
    print(f"Addition (A + B):\n{A + B}\n")
else:
    print("Addition not possible (Dimensions must match).\n")

# 4. Matrix Multiplication
if c1 == r2:
    print(f"Multiplication (A @ B):\n{A @ B}")
else:
    print("Multiplication not possible (Columns of A must equal Rows of B).")