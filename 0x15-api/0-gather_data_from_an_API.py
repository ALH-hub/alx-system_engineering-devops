#!/usr/bin/python3
"""gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [todo.get("title") for todo in todos
                 if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(task)) for task in completed]
