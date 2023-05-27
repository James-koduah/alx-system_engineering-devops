#!/usr/bin/python3

"""Use an Api of Employees todo and display tasks done"""
from urllib import request
import json
import sys


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
    user_name = ''
    titles = []

    user_name = user[id-1]["name"]

    for dicts in todo:
        if dicts["userId"] == id:
            total_tasks += 1
            if dicts["completed"] is True:
                total_tasks_done += 1
                titles.append(dicts["title"])


    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, total_tasks_done, total_tasks))
    for i in titles:
        print('\t {}'.format(i))
