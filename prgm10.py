# Import pandas library
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, 25, 22, 24, 26],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nBasic Information:")
print(df.info())
