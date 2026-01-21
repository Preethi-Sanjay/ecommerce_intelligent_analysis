import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned/ecommerce_cleaned.csv")

# Calculate KPIs
total_revenue = df['revenue'].sum()
total_orders = df['invoiceno'].nunique()
total_customers = df['customerid'].nunique()
avg_order_value = total_revenue / total_orders

# Print KPIs (for logs / interview proof)
print("BUSINESS KPIs")
print("------------------")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Average Order Value: {avg_order_value:,.2f}")

# -----------------------------
# KPI DASHBOARD (IMAGE)
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

kpi_text = (
    f"Total Revenue\n{total_revenue:,.2f}\n\n"
    f"Total Orders\n{total_orders}\n\n"
    f"Total Customers\n{total_customers}\n\n"
    f"Average Order Value\n{avg_order_value:,.2f}"
)

ax.text(
    0.5, 0.5,
    kpi_text,
    fontsize=16,
    ha='center',
    va='center',
    bbox=dict(boxstyle="round,pad=1", edgecolor="black")
)

plt.title("E-Commerce Business KPIs", fontsize=18)
plt.tight_layout()
plt.savefig("visuals/insights/kpi_dashboard.png")
plt.close()

print("KPI Dashboard done ")
