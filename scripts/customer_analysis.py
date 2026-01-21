import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/ecommerce_cleaned.csv")

customer_revenue = df.groupby('customerid')['revenue'].sum().sort_values(ascending=False)

top_customers = customer_revenue.head(10)

plt.figure()
top_customers.plot(kind='bar')
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visuals/insights/top_customers.png")
plt.close()

print("Top customers analysis completed.")
