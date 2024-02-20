#!/usr/bin/python3
"""gather data from an API"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userID = sys.argv[1]
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    username = user.get("username")

    with open("{}.json".format(userID), 'w') as file:
        json.dump({userID: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            } for todo in todos]}, file)
