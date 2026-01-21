import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned/ecommerce_cleaned.csv")

# Revenue by country (top 10)
country_revenue = (
    df.groupby('country')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Plot
plt.figure(figsize=(10, 6))
country_revenue.plot(kind='bar')
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save figure
plt.savefig("visuals/insights/revenue_by_country.png")
plt.close()

print("Revenue by country chart saved successfully.")
