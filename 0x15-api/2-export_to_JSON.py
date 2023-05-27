#!/usr/bin/python3

"""Use an Api of Employees todo and display tasks done"""
import json
import sys
from urllib import request


if __name__ == "__main__":
    todos = request.urlopen('https://jsonplaceholder.typicode.com/todos/',
                            data=None)
    users = request.urlopen('https://jsonplaceholder.typicode.com/users',
                            data=None)

    id = int(sys.argv[1])
    todo = json.load(todos)
    user = json.load(users)

    total_tasks = 0
    total_tasks_done = 0
    user_name = user[id-1]["name"]
    titles = []
    json_format = []

    for dicts in todo:
        if dicts["userId"] == id:
            total_tasks += 1
            if dicts["completed"] is True:
                total_tasks_done += 1
                titles.append(dicts["title"])
            task_dict = {
                    "task": f'{dicts["title"]}',
                    "completed": f'{dicts["completed"]}',
                    "username": f'{user[id-1]["username"]}'
                    }
            json_format.append(task_dict)

    final = {f"{id}": json_format}
    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, total_tasks_done, total_tasks))
    for i in titles:
        print('\t {}'.format(i))

    with open('{}.json'.format(id), 'w', encoding="UTF8") as f:
        json.dump(final, f)
