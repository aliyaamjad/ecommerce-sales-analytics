import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ecommerce_sales.csv")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

print("\n========== E-COMMERCE SALES ANALYTICS ==========\n")

# Show dataset
print("Sales Data:")
print(df)

# Dataset information
print("\n========== DATASET INFORMATION ==========\n")
print(df.info())

# Total revenue
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: ₹{total_revenue:,.0f}")

# Total quantity sold
total_quantity = df["Quantity"].sum()
print(f"Total Quantity Sold: {total_quantity}")

# Best-selling product by quantity
product_sales = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\n========== PRODUCT PERFORMANCE ==========\n")
print(product_sales)

best_product = product_sales.idxmax()
print(f"\nBest-Selling Product: {best_product}")

# Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\n========== CATEGORY REVENUE ==========\n")
print(category_revenue)

# Revenue by region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\n========== REGIONAL REVENUE ==========\n")
print(region_revenue)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Monthly revenue
monthly_revenue = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()

print("\n========== MONTHLY REVENUE ==========\n")
print(monthly_revenue)

# ---------------- CHART 1 ----------------

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Products Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- CHART 2 ----------------

plt.figure(figsize=(8, 5))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ---------------- CHART 3 ----------------

plt.figure(figsize=(8, 5))
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ---------------- CHART 4 ----------------

plt.figure(figsize=(8, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n========== BUSINESS INSIGHTS ==========\n")

print(f"1. Total revenue generated: ₹{total_revenue:,.0f}")
print(f"2. Total products sold: {total_quantity}")
print(f"3. Best-selling product: {best_product}")
print(f"4. Highest revenue category: {category_revenue.idxmax()}")
print(f"5. Highest revenue region: {region_revenue.idxmax()}")

print("\nAnalytics completed successfully! 🚀")











# ================= PROFESSIONAL DASHBOARD =================

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("E-Commerce Sales Analytics Dashboard",
             fontsize=18, fontweight="bold")

# 1. Products Sold
product_sales.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Products Sold")
axes[0, 0].set_xlabel("Product")
axes[0, 0].set_ylabel("Quantity")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Revenue by Category
category_revenue.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Revenue by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue (₹)")

# 3. Revenue by Region
region_revenue.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Revenue by Region")
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Revenue (₹)")

# 4. Monthly Revenue Trend
monthly_revenue.plot(kind="line", marker="o", ax=axes[1, 1])
axes[1, 1].set_title("Monthly Revenue Trend")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Revenue (₹)")
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

print("\n================ DASHBOARD SUMMARY ================")
print(f"Total Revenue       : ₹{total_revenue:,.0f}")
print(f"Total Units Sold    : {total_quantity}")
print(f"Best-Selling Product: {best_product}")
print(f"Top Category        : {category_revenue.idxmax()}")
print(f"Top Region          : {region_revenue.idxmax()}")
print(f"Best Revenue Month  : {monthly_revenue.idxmax()}")

print("\nProject Status: PROFESSIONAL ANALYTICS DASHBOARD READY 🚀")