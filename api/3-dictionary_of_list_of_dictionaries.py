#!/usr/bin/python3
"""Script to export data in JSON format"""

import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    users = requests.get(f'{API_URL}/users').json()
    todo_list = requests.get(f"{API_URL}/todos").json()

    json_filename = "todo_all_employees.json"

    data = {}

    for task in todo_list:

        user_id = task['userId']

        if user_id not in data:
            data[user_id] = []

        data[user_id].append({
            "username": next(user['username']
                             for user in users
                             if user['id'] == user_id),
            "task": task['title'],
            "completed": task['completed']
        })
    with open(json_filename, 'w') as file:
        json.dump(data, file)
