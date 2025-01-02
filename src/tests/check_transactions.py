import sys
import os

# Add the project root to the module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.database.db import get_all_transactions

transactions = get_all_transactions()
for tx in transactions:
    print(tx)
