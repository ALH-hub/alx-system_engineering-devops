#!/usr/bin/python3
"""gather data from an API"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userID = sys.argv[1]
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    username = user.get("username")

    with open("{}.csv".format(userID), 'w', newline="") as file:
        line = csv.writer(file, quoting=csv.QUOTE_ALL)
        [line.writerow(
            [userId, username, todo.get("completed"), todo.get("title")]
            for todo in todos)]
