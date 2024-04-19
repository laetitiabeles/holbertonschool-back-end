#!/usr/bin/python3
""" Script that exports data in the JSON format """

import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":

    employee_id = sys.argv[1]

    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()

    todo_list = requests.get("{}todos?userId={}".format(API_URL,
                                                        employee_id)).json()

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee.get("username")
            }
            for task in todo_list]}, json_file)
