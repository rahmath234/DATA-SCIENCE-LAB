import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, 25, 22, 24, 26],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nStudents with Marks > 85:")
print(df[df["Marks"] > 85])

print("\nStudents with Age >= 24:")
print(df[df["Age"] >= 24])

print("\nStudents with Age >= 24 and Marks > 85:")
print(df[(df["Age"] >= 24) & (df["Marks"] > 85)])

print("\nSelecting rows 1 to 3 and columns Name and Marks:")
print(df.loc[1:3, ["Name", "Marks"]])

print("\nStudents with Marks > 85 using .loc:")
print(df.loc[df["Marks"] > 85, ["Name", "Marks"]])
