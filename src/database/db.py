import sqlite3
import logging

# Database file path
DB_PATH = "src/database/transactions.db"

# Configure logging
logging.basicConfig(
    filename="src/logs/db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    Returns:
        Connection object: A connection to the database.
    """
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Access rows as dictionaries
        return conn
    except sqlite3.Error as e:
        logging.error(f"Failed to connect to the database: {e}")
        raise Exception("Database connection error")

def create_transactions_table():
    """
    Create the transactions table if it doesn't already exist.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feature1 REAL,
                feature2 REAL,
                feature3 REAL,
                feature4 REAL,
                feature5 REAL,
                result TEXT
            )
        ''')
        conn.commit()
        logging.info("Transactions table created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating transactions table: {e}")
    finally:
        conn.close()

def save_transaction(features, result):
    """
    Save a transaction to the database.
    Args:
        features (list): List of feature values.
        result (str): Prediction result ("Fraudulent" or "Not Fraudulent").
    """
    logging.info(f"Transaction attempted")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (feature1, feature2, feature3, feature4, feature5, result)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (*features, result))
        conn.commit()
        logging.info(f"Transaction saved: Features={features}, Result={result}")
    except sqlite3.Error as e:
        logging.error(f"Error saving transaction: {e}")
    finally:
        conn.close()

def get_all_transactions():
    """
    Retrieve all transactions from the database.
    Returns:
        list: A list of dictionaries representing all transactions.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transactions')
        rows = cursor.fetchall()
        logging.info("Fetched all transactions successfully.")
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        logging.error(f"Error fetching transactions: {e}")
        return []
    finally:
        conn.close()

# Add testing code here
if __name__ == "__main__":
    try:
        print("Creating transactions table...")
        create_transactions_table()
        print("Table created successfully!")

        print("Saving a sample transaction...")
        features = [10.2, 2.2, 12.36, 24.2, 5.2561]
        result = "Fraudulent"
        save_transaction(features, result)
        print("Sample transaction saved successfully!")

        print("Fetching all transactions...")
        transactions = get_all_transactions()
        print(f"Transactions: {transactions}")
    except Exception as e:
        print(f"Error: {e}")
