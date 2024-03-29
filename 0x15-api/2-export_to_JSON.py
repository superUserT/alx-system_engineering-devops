#!/usr/bin/python3
import requests
import json
import sys


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    return user_data, todo_data


def export_to_json(employee_id, user_data, todo_data):
    file_name = f"{employee_id}.json"

    data_to_export = {str(employee_id):[{
        "task": task["title"], "completed": task["completed"],
        "username": user_data["username"]} for task in todo_data]}

    with open(file_name, 'w') as json_file:
        json.dump(data_to_export, json_file, indent=2)

    print(f"Data exported to {file_name}")


def display_todo_progress(employee_id):
    user_data, todo_data = fetch_employee_data(employee_id)

    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task["completed"]]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

    export_to_json(employee_id, user_data, todo_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)
