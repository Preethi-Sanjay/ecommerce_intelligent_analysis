import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned/ecommerce_cleaned.csv")

# Convert invoicedate to datetime (FIX)
df['invoicedate'] = pd.to_datetime(df['invoicedate'])

# Create month column
df['month'] = df['invoicedate'].dt.to_period('M')

# Monthly revenue calculation
monthly_revenue = df.groupby('month')['revenue'].sum()

# Plot
plt.figure()
monthly_revenue.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visuals/insights/monthly_revenue.png")
plt.close()

print("Trend analysis completed successfully.")
