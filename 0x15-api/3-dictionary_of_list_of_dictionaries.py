#!/usr/bin/python3
'''
Exports to CSV
'''
import json
import requests
import sys


if __name__ == "__main__":

    # api-endpoint
    url = "https://jsonplaceholder.typicode.com/"

    # Sending a request to get users
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()

    # Sending a request to get todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    all_tasks = {}

    '''
    exports to a json file
    '''

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                task_list.append(taskDict)
        all_tasks[user.get('id')] = task_list
    with open('todo_all_employees.json', mode='w') as user_id:
        json.dump(all_tasks, user_id)
