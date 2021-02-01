#!/usr/bin/python3
'''
Exports to CSV
'''
import requests
from sys import argv
import csv


if __name__ == "__main__":

    '''
    api-endpoint
    '''

    url = "https://jsonplaceholder.typicode.com/"

    '''
     Sending a request to get users
    '''

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1].json()))

    '''
    Sending a request to get todos
    '''

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv[1].json()))

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
        user.get("name"), len(finished_tasks), len(todos)))

    '''
    2nd line / n lines : display the title of completed tasks:
    '''

    [print("\t {}".format(finished)) for finished in finished_tasks]

    '''
    exports to a csv file
    '''

    with open("{}.csv".format(sys.argv[1]), "w") as user_id:
        for line in finished_tasks:
            user_id.write(line + "\n")
