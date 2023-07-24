#!/usr/bin/python3
"""Return info about a todo list and export to csv format"""


if __name__ == '__main__':
    import csv
    import json
    import requests
    import sys

    user_id = int(sys.argv[1])

    todo_r = requests.get('https://jsonplaceholder.typicode.com/todos')
    user_r = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = json.loads(todo_r.content)
    users = json.loads(user_r.content)
    user = ''
    username = ''
    user_tasks = []
    completed_tasks = []
    to_csv = []
    for p in users:
        if p['id'] == user_id:
            user = p
            username = user['username']
            break
    for todo in todos:
        if todo['userId'] == user_id:
            user_tasks.append(todo)
            if todo['completed'] is True:
                completed_tasks.append(todo)

    print('Employee {} is done with tasks({}/{}):'.
          format(user['name'], len(completed_tasks), len(user_tasks)))


    for task in completed_tasks:
        print('\t {}'.format(task['title']))


    for task in user_tasks:
        status = task['completed']
        title = task['title']
        info = [user_id, username, status, title]
        to_csv.append(info)

    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row in to_csv:
            writer.writerow(row)
