import pandas as pd

# Specify the file path for the CSV data
filepath = 'data/orders.csv'

def read_orders_data(file_path):
    try:
        # Read orders data from a CSV file.
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def compute_monthly_revenue(df):
    # Compute total revenue by month.
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.strftime('%B %Y')
    df['total'] = df['product_price'] * df['quantity']
    monthly_revenue = df.groupby('month')['total'].sum()
    
    # Sort the index to display months in chronological order.
    monthly_revenue = monthly_revenue.reindex(pd.to_datetime(monthly_revenue.index, format='%B %Y').sort_values().strftime('%B %Y'))
    
    # Set a custom name for the Series
    monthly_revenue.name = "total"

    return monthly_revenue

def compute_product_revenue(df):
    # Compute total revenue by product.

    df['total'] = df['product_price'] * df['quantity']
    product_revenue = df.groupby('product_name')['total'].sum()
    
    # Set a custom name for the Series
    product_revenue.name = "total"

    return product_revenue

def compute_customer_revenue(df):
    # Compute total revenue by customer.
    df['total'] = df['product_price'] * df['quantity']
    customer_revenue = df.groupby('customer_id')['total'].sum()

    # Set a custom name for the Series
    customer_revenue.name = "total"

    return customer_revenue

def identify_top_customers(df, n=10):
    # Identify the top N customers by revenue generated.

    df['total'] = df['product_price'] * df['quantity']
    top_customers = df.groupby('customer_id')['total'].sum().nlargest(n)

    # Set a custom name for the Series
    top_customers.name = "total"

    return top_customers, n

if __name__ == "__main__":
    orders_df = read_orders_data(filepath)

    if orders_df is not None:
        monthly_revenue = compute_monthly_revenue(orders_df)
        product_revenue = compute_product_revenue(orders_df)
        customer_revenue = compute_customer_revenue(orders_df)
        top_customers, n = identify_top_customers(orders_df)

        # Results 
        print("\n")
        print("**** Monthly Revenue ****")
        print(monthly_revenue)
        print("\n")

        print("**** Product Revenue ****")
        print(product_revenue)
        print("\n")

        print("**** Customer Revenue ****")
        print(customer_revenue)
        print("\n")

        print(f"**** Top {n} Customers by Revenue ****")
        print(top_customers)
