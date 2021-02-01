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
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()

    # Sending a request to get todos
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    '''
    checks if a task is completed by sending
    a get request to check the list of completed tasks
    '''

    finished_tasks = [task.get("title") for task in todos if
                      task.get("completed") is True]

    '''
    1st line : Ex Employee Ervin Howell is done with tasks(8/20)
    '''

    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(finished_tasks), len(todos)))

    '''
    2nd line / n lines : display the title of completed tasks:
    '''

    [print("\t {}".format(finished)) for finished in finished_tasks]

    '''
    exports to a json file
    '''

    with open("{}.json".format(sys.argv[1]), "w") as user_id:
            json.dump({sys.argv[1]: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': users.get('username')
            } for task in todos]}, user_id)
