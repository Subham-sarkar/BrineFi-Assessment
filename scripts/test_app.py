import pandas as pd
import pytest
from app import (
    compute_monthly_revenue,
    compute_product_revenue,
    compute_customer_revenue,
    identify_top_customers,
)

# Define a fixture to load the sample data for testing
@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5],
        'customer_id': ['CUST-001', 'CUST-002', 'CUST-003', 'CUST-001', 'CUST-004'],
        'order_date': ['2022-08-01', '2022-08-01', '2022-09-01', '2022-09-01', '2022-10-01'],
        'product_id': ['PROD-001', 'PROD-002', 'PROD-003', 'PROD-004', 'PROD-005'],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'product_price': [10.0, 20.0, 30.0, 40.0, 50.0],
        'quantity': [2, 1, 3, 2, 1],
    }
    return pd.DataFrame(data)

# Test the compute_monthly_revenue function
def test_compute_monthly_revenue(sample_data):
    monthly_revenue = compute_monthly_revenue(sample_data)
    expected_result = pd.Series({
        'August 2022': 40.0, 
        'September 2022': 170.0, 
        'October 2022': 50.0,
        }, name='total')
    
    print("\n")
    print(sample_data)
    print("\nTestcases for compute_monthly_revenue function\n")
    print("**** Computed Result ****\n")
    print(monthly_revenue)
    print("\n**** Expected Result ****\n")
    print(expected_result)
    
    pd.testing.assert_series_equal(monthly_revenue, expected_result, check_dtype=False, check_index=False)

    print("\n******************************************************\n")

# Test the compute_product_revenue function
def test_compute_product_revenue(sample_data):
    product_revenue = compute_product_revenue(sample_data)
    expected_result = pd.Series({
        'Product A': 20.0,
        'Product B': 20.0,
        'Product C': 90.0,
        'Product D': 80.0,
        'Product E': 50.0,
    }, name='total')

    print("\n")
    print(sample_data)
    print("\nTestcases for compute_product_revenue function\n")
    print("**** Computed Result ****\n")
    print(product_revenue)
    print("\n**** Expected Result ****\n")
    print(expected_result)

    pd.testing.assert_series_equal(product_revenue, expected_result, check_dtype=False, check_index=False)

    print("\n******************************************************\n")

# Test the compute_customer_revenue function
def test_compute_customer_revenue(sample_data):
    customer_revenue = compute_customer_revenue(sample_data)
    expected_result = pd.Series({
        'CUST-001': 100.0,
        'CUST-002': 20.0,
        'CUST-003': 90.0,
        'CUST-004': 50.0,
    }, name='total')

    print("\n")
    print(sample_data)
    print("\nTestcases for compute_customer_revenue function\n")
    print("**** Computed Result ****\n")
    print(customer_revenue)
    print("\n**** Expected Result ****\n")
    print(expected_result)
    
    pd.testing.assert_series_equal(customer_revenue, expected_result, check_dtype=False, check_index=False)

    print("\n******************************************************\n")

# Test the identify_top_customers function
def test_identify_top_customers(sample_data):
    top_customers, n = identify_top_customers(sample_data, n=3)
    expected_result = pd.Series({
        'CUST-001': 100.0,
        'CUST-003': 90.0,
        'CUST-004': 50.0,
    }, name='total')

    print("\n")
    print(sample_data)
    print("\nTestcases for identify_top_customers function\n")
    print("**** Computed Result ****\n")
    print(top_customers)
    print("\n**** Expected Result ****\n")
    print(expected_result)
     
    pd.testing.assert_series_equal(top_customers, expected_result, check_dtype=False, check_index=False)

    print("\n******************************************************\n")

# Run the tests
if __name__ == "__main__":
    pytest.main()
    
