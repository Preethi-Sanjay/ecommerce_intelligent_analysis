import pandas as pd

df = pd.read_csv("data/raw/online_retail.csv")

print("Initial shape:", df.shape)

# Remove cancelled invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Drop missing values
df = df.dropna()

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Remove negative or zero values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Standardize column names
df.columns = df.columns.str.lower()

df.to_csv("data/cleaned/ecommerce_cleaned.csv", index=False)

print("Cleaning complete.")
print("Final shape:", df.shape)
