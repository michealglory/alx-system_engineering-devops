#!/usr/bin/python3
"""This script retrieves information about an employee's completed tasks
from the JSONPlaceholder API.

Usage:
    python script.py <employee_id>

Parameters:
    - employee_id (str): The ID of the employee whose task completion
    information is to be retrieved.

The script fetches employee details and tasks from the JSONPlaceholder API
based on the provided employee ID. It then prints the employee's name and
the list of completed tasks along with a summary of the completion status.

Example:
    python script.py 1"""


import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

