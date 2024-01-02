#!/usr/bin/python3
"""Export data in JSON format."""
import json
import requests
from sys import argv


def dict_to_json():
    url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(url).json()
    users = requests.get(users_url).json()

    tasks_by_user = {}

    for todo in todos:
        user_id = todo["userId"]
        task_info = {
            "username": [user["username"] for user in users if user["id"] == user_id][0],
            "task": todo["title"],
            "completed": todo["completed"],
        }
        if user_id in tasks_by_user:
            tasks_by_user[user_id].append(task_info)
        else:
            tasks_by_user[user_id] = [task_info]


    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file)


if __name__ == "__main__":
    dict_to_json()
