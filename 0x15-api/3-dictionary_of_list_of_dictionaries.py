#!/usr/bin/python3
"""Export todo tasks for all users to a JSON file

This module exports todo task data for all users from
theJSONPlaceholder fake API to a local JSON file.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        id_user = user.get('id')
        name_user = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_user)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[id_user] = []
        for task in tasks:
            dictionary[id_user].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name_user
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
