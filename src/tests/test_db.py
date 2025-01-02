import sys
import os

# Add the project root to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.database.db import create_transactions_table, save_transaction, get_all_transactions

def test_database_operations():
    """
    Test all database operations:
    - Table creation.
    - Saving transactions.
    - Retrieving transactions.
    """

    print("Creating transactions table...")
    create_transactions_table()
    print("Table created successfully!")

    print("Saving a transaction...")
    features = [1.2, 2.3, 3.4, 4.5, 5.6]
    result = "Fraudulent"
    save_transaction(features, result)
    print("Transaction saved successfully!")

    print("Fetching all transactions...")
    transactions = get_all_transactions()
    print(f"Transactions: {transactions}")

    assert len(transactions) > 0, "No transactions found in the database!"
    assert transactions[0]["feature1"] == 1.2, "Feature1 value is incorrect!"
    assert transactions[0]["result"] == "Fraudulent", "Result value is incorrect!"
    print("All tests passed!")

if __name__ == "__main__":
    test_database_operations()
