import csv

data = [
    ["id", "date", "product", "price", "quantity"],
    [101, "2026-02-15", "Laptop", 1200, 1],
    [102, "2026-02-15", "Mouse", 25, 2],
    [103, "2026-02-15", "Keyboard", 45, 1],
    [104, "2026-02-15", "Monitor", 300, 2],
    [105, "2026-02-15", "HDMI Cable", 10, 5]
]

with open("sales_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("sales_data.csv created successfully!")