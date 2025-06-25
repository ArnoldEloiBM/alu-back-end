#!/usr/bin/python3
"""Export all employees' TODO data to JSON format."""
import json
import requests


def export_all_to_json():
    """Export all employees' TODO data to JSON file."""
    try:
        # Base API URL
        base_url = "https://jsonplaceholder.typicode.com"
        
        # Fetch all users
        users = requests.get(f"{base_url}/users").json()
        
        # Fetch all todos
        todos = requests.get(f"{base_url}/todos").json()
        
        # Prepare data structure
        all_data = {}
        
        for user in users:
            user_id = str(user["id"])
            user_todos = [todo for todo in todos if todo["userId"] == user["id"]]
            
            all_data[user_id] = [
                {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in user_todos
            ]
        
        # Write to JSON file
        with open("todo_all_employees.json", 'w') as jsonfile:
            json.dump(all_data, jsonfile)
            
    except requests.exceptions.RequestException:
        print("Error fetching data")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    export_all_to_json()
