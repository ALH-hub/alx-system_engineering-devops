#!/usr/bin/python3
"""gather data from an API"""

import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    with open("todo_all_employees.json", 'w') as file:
        for user in users:
            todos_user = requests.get(todo_url, params={"userId": user.get("id")}).json()
            json.dump({user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
                } for todo in todos_user]}, file)
