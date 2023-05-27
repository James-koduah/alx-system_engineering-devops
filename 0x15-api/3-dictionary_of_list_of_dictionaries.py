#!/usr/bin/python3

"""Use an Api of Employees todo and display tasks done"""
import json
import sys
from urllib import request


if __name__ == "__main__":
    todos = request.urlopen('https://jsonplaceholder.typicode.com/todos/',
                            data=None)
    userss = request.urlopen('https://jsonplaceholder.typicode.com/users',
                             data=None)

    todo = json.load(todos)
    users = json.load(userss)

    user_ids = []
    final_boss = {}
    for user in users:
        user_ids.append(user["id"])

    for id in user_ids:
        json_format = []
        for dicts in todo:
            if dicts["userId"] == id:
                task_dict = {
                        "username": f'{users[id-1]["username"]}',
                        "task": f'{dicts["title"]}',
                        "completed": f'{dicts["completed"]}'
                        }
                json_format.append(task_dict)
        final_boss[id] = json_format
    with open('todo_all_employees.json'.format(id), 'w', encoding="UTF8") as f:
        json.dump(final_boss, f)
