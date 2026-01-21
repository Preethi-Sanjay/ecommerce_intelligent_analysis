import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/ecommerce_cleaned.csv")

product_revenue = df.groupby('description')['revenue'].sum().sort_values(ascending=False).head(10)

plt.figure()
product_revenue.plot(kind='barh')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("visuals/insights/top_products.png")
plt.close()

print("Product analysis completed.")
