#!/usr/bin/python3
"""Fetches employee details and tasks from JSONPlaceholder API and writes
them to a CSV file.

    Args:
        employee_id (str): The ID of the employee.

    Returns:
        None"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))
