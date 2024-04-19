#!/usr/bin/python3
""" Script that exports data for all employees in the JSON format """

import json
import requests


API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":

    employees = requests.get('{}users'.format(API_URL)).json()

    todos_list = requests.get("{}todos".format(API_URL)).json()

    all_employees_data = {}

    for employee in employees:
        user_id = employee.get("id")
        username = employee.get("username")

        employee_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos_list if task["userId"] == user_id
        ]
        all_employees_data[user_id] = employee_tasks

    json_file = "todo_all_employees.json"

    with open(json_file, "w") as json_file:
        json.dump(all_employees_data, json_file)
