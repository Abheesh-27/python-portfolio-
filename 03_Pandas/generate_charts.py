import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(
    "03_Pandas/Sample_Superstore.csv",
    encoding="latin1"
)

# -----------------------------
# DATA CLEANING
# -----------------------------
df = df.drop_duplicates()

if df["Postal Code"].isnull().sum() > 0:
    df["Postal Code"] = df["Postal Code"].fillna(
        df["Postal Code"].median()
    )

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Order Year"] = df["Order Date"].dt.year
df["Order Month_Year"] = df["Order Date"].dt.to_period("M").astype(str)

df["Discount_Level"] = df["Discount"].apply(
    lambda x: "Low Discount" if x <= 0.2 else "High Discount"
)

# -----------------------------
# CREATE IMAGES FOLDER
# -----------------------------
os.makedirs("03_Pandas/images", exist_ok=True)

# -----------------------------
# 1. SALES BY CATEGORY
# -----------------------------
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("03_Pandas/images/sales_by_category.png")
plt.close()

# -----------------------------
# 2. PROFIT BY CATEGORY
# -----------------------------
category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("03_Pandas/images/profit_by_category.png")
plt.close()

# -----------------------------
# 3. YEARLY SALES TREND
# -----------------------------
yearly_sales = (
    df.groupby("Order Year")["Sales"]
    .sum()
)

plt.figure(figsize=(8,5))
yearly_sales.plot(marker="o")
plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("03_Pandas/images/yearly_sales_trend.png")
plt.close()

# -----------------------------
# 4. MONTHLY SALES TREND
# -----------------------------
monthly_sales = (
    df.groupby("Order Month_Year")["Sales"]
    .sum()
)

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("03_Pandas/images/monthly_sales_trend.png")
plt.close()

# -----------------------------
# 5. DISCOUNT VS PROFIT
# -----------------------------
discount_profit = (
    df.groupby("Discount")["Profit"]
    .mean()
)

plt.figure(figsize=(8,5))
discount_profit.plot(marker="o")
plt.title("Average Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig("03_Pandas/images/discount_vs_profit.png")
plt.close()

# -----------------------------
# 6. CATEGORY VS REGION HEATMAP
# -----------------------------
pivot = pd.pivot_table(
    df,
    values="Profit",
    index="Category",
    columns="Region",
    aggfunc="sum"
)

plt.figure(figsize=(8,4))
plt.imshow(pivot, aspect="auto")

plt.colorbar(label="Profit")

plt.xticks(
    range(len(pivot.columns)),
    pivot.columns
)

plt.yticks(
    range(len(pivot.index)),
    pivot.index
)

plt.title("Profit by Category and Region")

plt.tight_layout()

plt.savefig("03_Pandas/images/category_region_heatmap.png")

plt.close()

print("\nCharts successfully generated!")

print("""
Generated Files
---------------
sales_by_category.png
profit_by_category.png
yearly_sales_trend.png
monthly_sales_trend.png
discount_vs_profit.png
category_region_heatmap.png
""")