import pandas as pd

print('\n===== SUPERSTORE DATA ANALYSIS =====')
df = pd.read_csv('03_Pandas/Sample_Superstore.csv', encoding='latin1')

print(df.head())

print('\nDATASET SHAPE:')
print(df.shape)

print('\nCOLUMN NAMES:')
print(df.columns.tolist())

print('\nDATA TYPES:')
print(df.dtypes)

print('\nMISSING VALUES:')
print(df.isnull().sum())

print('\nDUPLICATED VALUES:')
print(df.duplicated().sum())


# DATA CLEANING
print('\n===== DATA CLEANING =====')

# Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
duplicates_after = df.duplicated().sum()

print(f'Duplicates before cleaning : {duplicates_before}')
print(f'Duplicates after cleaning  : {duplicates_after}')

# Handle missing values (if present)
if df['Postal Code'].isnull().sum() > 0:
    df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].median())

print('\nRemaining Missing Values:')
print(df.isnull().sum())

# currently order date & ship date are in string format , we need to convert it to datetime

print('\n===== CONVERTING DATE COLUMNS =====')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print(df[['Order Date', 'Ship Date']].dtypes)

print('\nUPDATED DATA TYPES:')
print(df.dtypes)


print('\n===== CREATING DATE COLUMNS =====')

df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month_Name'] = df['Order Date'].dt.month_name()
df['Order Day'] = df['Order Date'].dt.day_name()

# Calculating shipping days 

df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

print(
    df[
        [
            "Order Date",
            "Ship Date",
            "Order Year",
            "Order Month",
            "Order Month_Name",
            "Order Day",
            "Shipping Days"
        ]
    ].head()
)

print('\n===== SALES USING APPLY() & LAMBDA =====')

df['Profit Status'] = df['Profit'].apply(
    lambda x: "Profit" if x > 0 
    else 'Loss' if x < 0
    else 'Break-even'
)

df['Sales Category'] = df['Sales'].apply(
    lambda x: 'High' if x >= 500 else 'Low'
)

df['Discount Category'] = df['Discount'].apply(
    lambda x: 'High Discount' if x >= 0.3 else 'Low Discount'
)

print(
    df[
        [
            "Sales",
            "Sales Category",
            "Discount",
            "Discount Category",
            "Profit",
            "Profit Status"
        ]
    ].head(10)
)


print("\n===== UPDATED DATASET SHAPE =====")
print(df.shape)

print("\n===== UPDATED COLUMNS =====")
print(df.columns.tolist())


print('\n===== GROUPBY() ANALYSIS =====')

category_sales = (
    df.groupby('Category')['Sales']
    .sum()
    .sort_values(ascending = False)
)
print('\nSALES BY CATEGORY:')
print(category_sales)


category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending = False)
)
print("\nPROFIT BY CATEGORY:")
print(category_profit)


category_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending = False)
)
print("\nQUANTITY BY CATEGORY:")
print(category_quantity)


# Multiple Aggregations
print('\n===== CATEGORY PERFORMANCE =====')

category_performance = df.groupby('Category').agg(
    Total_Sales = ("Sales", 'sum'),
    Total_Quantity = ("Quantity", 'sum'),
    Average_Discount = ("Discount", 'mean'),
    Total_Profit = ("Profit", 'sum')
    ).sort_values(
        by = "Total_Sales",
        ascending = False
    )

print(category_performance)

# Calculate profit marigin
category_performance["Profit_Margin"] = (
    category_performance["Total_Profit"]
    / category_performance["Total_Sales"]
) * 100

print("\nCATEGORY PERFORMANCE WITH PROFIT MARGIN:")
print(category_performance)

# most profitable category 
most_profitable_category = category_performance['Total_Profit'].idxmax()

print('\nMOST PROFITABLE CATEGORY:')
print(most_profitable_category)

# best margin category
best_margin_category = category_performance['Profit_Margin'].idxmax()

print('\nCATEGORY WITH BEST PROFIT MARGIN:')
print(best_margin_category)


print("\n===== REGIONAL PERFORMANCE =====")

region_performance = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Discount=("Discount", "mean")
).sort_values(
    by = "Total_Sales",
    ascending = False
)

# best-performing region
region_performance["Profit_Margin"] = (
    region_performance["Total_Profit"]
    / region_performance["Total_Sales"]
) * 100

print(region_performance)

best_region = region_performance["Total_Sales"].idxmax()

print("\nBest Region by Sales:")
print(best_region)

# most profitable region
most_profitable_region = region_performance["Total_Profit"].idxmax()

print("\nMost Profitable Region:")
print(most_profitable_region)


print("\n===== SUB-CATEGORY PERFORMANCE =====")

subcategory_performance = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Average_Discount=("Discount", "mean")
).sort_values(
    by = "Total_Profit",
    ascending = False
)

subcategory_performance["Profit_Margin"] = (
    subcategory_performance["Total_Profit"]
    / subcategory_performance["Total_Sales"]
) * 100

print(subcategory_performance)

print("\n===== TOP 5 SUB-CATEGORIES BY PROFIT =====")

print(
    subcategory_performance
    .sort_values(
        by = "Total_Profit",
        ascending = False
    )
    .head(5)
)

print("\n===== BOTTOM 5 SUB-CATEGORIES BY PROFIT =====")

print(
    subcategory_performance
    .sort_values(
        by = "Total_Profit",
        ascending = True
    )
    .head(5)
)

print("\n===== LOSS-MAKING PRODUCTS =====")

loss_product_analysis = (
    df[df["Profit"] < 0]
    .groupby("Product Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Average_Discount=("Discount", "mean")
    )
    .sort_values(
        by = "Total_Profit",
        ascending = True
    )
)

print("\n===== TOP 10 LOSS-MAKING PRODUCTS =====")
print(loss_product_analysis.head(10))


print("\n===== DISCOUNT VS PROFIT ANALYSIS =====")

discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean"),
    Number_of_Records=("Order ID", "count")
)

discount_analysis["Profit_Margin"] = (
    discount_analysis["Total_Profit"]
    / discount_analysis["Total_Sales"]
) * 100

print(discount_analysis)


print("\n===== LOW VS HIGH DISCOUNT ANALYSIS =====")

df["Discount_Level"] = df["Discount"].apply(
    lambda x: "Low Discount" if x <= 0.2 else "High Discount"
)

discount_level_analysis = df.groupby("Discount_Level").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Discount=("Discount", "mean"),
    Number_of_Records=("Order ID", "count")
)

discount_level_analysis["Profit_Margin"] = (
    discount_level_analysis["Total_Profit"]
    / discount_level_analysis["Total_Sales"]
) * 100

print(discount_level_analysis)

print('\n===== TOP 10 CUSTOMERS BY SALE =====')
top_customers = (
    df.groupby('Customer Name')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    )
    .sort_values(
        by = 'Total_Sales',
        ascending = False
    )
    .head(10)
)

print(top_customers)

print("\n===== TOP 10 CUSTOMERS BY PROFIT =====")

top_profit_customers = (
    df.groupby("Customer Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values(
        by = "Total_Profit",
        ascending = False
    )
    .head(10)
)

print(top_profit_customers)

print("\n===== TOP 10 LOSS-MAKING CUSTOMERS =====")

loss_customers = (
    df.groupby("Customer Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values(
        by = "Total_Profit",
        ascending = True
    )
    .head(10)
)

print(loss_customers)

print("\n===== YEARLY PERFORMANCE =====")

yearly_performance = df.groupby("Order Year").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

yearly_performance["Profit_Margin"] = (
    yearly_performance["Total_Profit"]
    / yearly_performance["Total_Sales"]
) * 100

print(yearly_performance)

print("\n===== MONTHLY PERFORMANCE =====")

df["Order Month_Year"] = df["Order Date"].dt.to_period("M")

monthly_performance = df.groupby("Order Month_Year").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print(monthly_performance)

print('\n===== CATEGORY VS REGION PIVOT TABLE =====')

category_region_pivot = pd.pivot_table(
    df,
    values = 'Profit',
    index = 'Category',
    columns = 'Region',
    aggfunc = 'sum'
)

print(category_region_pivot)

print('\n===== CATEGORY VS REGION SALES PIVOT TABLE =====')

category_region_sales_pivot = pd.pivot_table(
    df,
    values = 'Sales',
    index = 'Category',
    columns = 'Region',
    aggfunc = 'sum'
)

print(category_region_sales_pivot)