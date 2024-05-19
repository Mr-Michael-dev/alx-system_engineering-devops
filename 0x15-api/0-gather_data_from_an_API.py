#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
using REST API
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print(f"Usage: {sys.argv[0]} <employee ID>")
        exit()

    user_id = int(sys.argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    EMPLOYEE = ""
    TOTAL_TASKS = 0
    DONE = 0

    for user in users:
        if user.get('id') == user_id:
            EMPLOYEE = user.get('name')

    for todo in todos:
        if todo.get('userId') == user_id:
            TOTAL_TASKS += 1
            if todo.get('completed') is True:
                DONE += 1

    print(f"Employee {EMPLOYEE} is done with tasks ({DONE}/{TOTAL_TASKS}):")

    for task in todos:
        if task.get('userId') == user_id:
            if task.get('completed') is True:
                print(f"\t{task['title']}")
