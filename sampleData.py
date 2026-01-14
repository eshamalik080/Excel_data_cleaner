import pandas as pd
from random import randint, choice

data = {
    "OrderID": [1001, 1002, 1003, 1003, 1004, 1005],
    "Product": ["Laptop", "Mouse", "Chair", "Chair", "Table", None],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Furniture", "Electronics"],
    "Quantity": [2, 5, None, 1, 3, 4],
    "Price": [800, 20, 150, None, 300, 50],
    "Date": pd.date_range(start="2024-01-01", periods=6)
}

df = pd.DataFrame(data)
df.to_excel("input_data.xlsx", index=False)
print("Sample Exel file created successfuly")
