#!/usr/bin/python3
"""Retrieve and display employee TODO list progress."""
import requests
import sys


def main():
    """Main function to fetch and display employee TODO progress."""
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    try:
        employee_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/users/{employee_id}/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()
        completed = [t['title'] for t in todos if t['completed']]

        print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")
        for task in completed:
            print(f"\t {task}")

    except requests.exceptions.RequestException:
        sys.exit("Error fetching data")
    except ValueError:
        sys.exit("Invalid employee ID")


if __name__ == "__main__":
    main()
