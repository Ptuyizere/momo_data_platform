import sys
import json
import time
from pathlib import Path


json_file = Path("../data/processed/modified_sms_v2.json")

transactions = []
transactions_dict = {}
next_id = 1

def load_data():
    """Loads json objects into a list in memory from the parsed json file"""
    global transactions, next_id
    
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            transactions = json.load(f)
    else:
        print("Records Json file does not exist.")
        sys.exit(1)
    
    # make sure every trans has an integer id
    for i, tr in enumerate(transactions, start=1):
        tr["id"] = i
    next_id = len(transactions) + 1

def list_to_dict(transactions):
    """Function transforms the list of transactions into a dictionary where keys are IDs"""
    global transactions_dict
    for transaction in transactions:
        tid = transaction["id"]
        transactions_dict[tid] = transaction

def search_list(id_list):
    results = []
    for id in id_list:
        for tr in transactions:
            if id == tr["id"]:
                results.append(tr)
    
    return results

def search_dict(id_list):
    results = []
    for id in id_list:
        results.append(transactions_dict[id])
    
    return results


if __name__ == "__main__":
    load_data()
    list_to_dict(transactions)

    print("First we test the linear search on the list of transactions")
    start_time = time.time()
    result = search_list([45, 76, 20, 50, 30, 56, 900, 1200, 9, 1, 90, 100, 200, 80, 33, 44, 3, 66, 77, 99])
    end_time = time.time()
    print(f"Execution time for linear search is: {end_time - start_time:.6f} seconds")

    print("Now we test the dictionary search")
    start_time = time.time()
    result = search_dict([45, 76, 20, 50, 30, 56, 900, 1200, 9, 1, 90, 100, 200, 80, 33, 44, 3, 66, 77, 99])
    end_time = time.time()
    print(f"Execution time for dictionary search is: {end_time - start_time:.6f} seconds")
