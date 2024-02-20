#!/usr/bin/python3
"""gather data from an API"""

import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user_url).json()

    with open("todo_all_employees.json", 'w') as file:
        json.dump({user.get("id"): [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
            } for todo in requests.get(
                todo_url, params={"userId": user.get("id")}).json()]
                   for user in users}, file)
