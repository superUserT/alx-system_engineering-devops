#!/usr/bin/python3
import json
import requests
from sys import argv


def list_of_dictionary():

    base_url = "https://jsonplaceholder.typicode.com"

    if len(argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        exit(1)

    employee_id = argv[1]

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    user_tasks = {"username": username, "tasks": []}

    for task in tasks_data:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": username,
        }
        user_tasks["tasks"].append(task_info)

    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump({employee_id: user_tasks["tasks"]}, json_file)

    print(f"Tasks for user {employee_id} exported to {filename}")


if __name__ == "__main__":
    list_of_dictionary()