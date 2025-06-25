#!/usr/bin/python3
"""
Using a REST API to return info about their TODO list.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    
    try:
        uid = sys.argv[1]
        user = requests.get(f"https://jsonplaceholder.typicode.com/users/{uid}").json()
        todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{uid}/todos").json()
        done = [t['title'] for t in todos if t['completed']]
        print(f"Employee {user['name']} is done with tasks({len(done)}/{len(todos)}):")
        [print(f"\t {task}") for task in done]
    except Exception:
        sys.exit("Error fetching data")