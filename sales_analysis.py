import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sales_data.csv')

# Display first few rows
print("Initial Data Preview:")
print(df.head())

# Clean the data
df['Date'] = pd.to_datetime(df['Date'])  # Convert Date to datetime format
df.dropna(inplace=True)  # Remove missing values (if any)

# Add a new column: Total Sale = Price * Quantity
df['Total_Sale'] = df['Price'] * df['Quantity']

# ------------------------
# Basic Data Analysis
# ------------------------

# 1. Total Sales
total_sales = df['Total_Sale'].sum()
print(f"\nTotal Sales: ${total_sales}")

# 2. Most Sold Products
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\nMost Sold Products:")
print(product_sales)

# 3. Sales by Category
category_sales = df.groupby('Category')['Total_Sale'].sum()
print("\nSales by Category:")
print(category_sales)

# 4. Sales Over Time
daily_sales = df.groupby('Date')['Total_Sale'].sum()

# ------------------------
# Data Visualization
# ------------------------

# Bar chart: Most sold products
product_sales.plot(kind='bar', color='skyblue')
plt.title('Most Sold Products')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.tight_layout()
plt.show()

# Pie chart: Sales by category
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales by Category')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Line chart: Daily sales trend
daily_sales.plot(kind='line', marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
