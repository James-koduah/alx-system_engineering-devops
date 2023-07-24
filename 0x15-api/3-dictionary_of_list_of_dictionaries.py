#!/usr/bin/python3
"""Return info about a todo list"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    todo_r = requests.get('https://jsonplaceholder.typicode.com/todos')
    user_r = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = json.loads(todo_r.content)
    users_all = json.loads(user_r.content)
    to_json = {}
    users = []

    for p in users_all:
        if p['id'] in users:
            pass
        else:
            users.append(str(p['id']))
    for user in users:
        user_tasks = []
        to_json_tasks = []
        username = ''
        for p in users_all:
            if p['id'] == int(user):
                username = p['username']
                break

        for todo in todos:
            if todo['userId'] == int(user):
                user_tasks.append(todo)

        for task in user_tasks:
            task_obj = {}
            task_obj['task'] = task['title']
            task_obj['completed'] = task['completed']
            task_obj['username'] = username
            to_json_tasks.append(task_obj)

        to_json[user] = to_json_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(to_json, f)
