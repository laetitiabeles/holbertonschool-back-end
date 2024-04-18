#!/usr/bin/env python3
""" Script that returns 'to-do list' info for a given employee ID """


import requests
import sys
import csv

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":

    employee_id = sys.argv[1]

    employee = requests.get(API_URL + "users/{}".format(employee_id)).json()

    todo_list = requests.get("{}todos?userId={}".format(API_URL,
                                                        employee_id)).json()

    with open("{}.csv".format(employee_id), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            writer.writerow([
                employee_id,
                employee.get("username"),
                task.get("completed"),
                task.get("title")
            ])