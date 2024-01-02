#!/usr/bin/python3

"""
Module for task 0
It requests data from a RESTful API
(https://jsonplaceholder.typicode.com)
and returns information about an employees tasks
"""

from requests import get
from sys import argv

def todo_progress():
    """
    Fetches the progress of a to-do list for a specific employee from a RESTful API.

    Args:
        None

    Returns:
        None

    Example Usage:
        python script.py 1

    This function can be used by running a Python
    script with the employee ID as a command line argument.
    It will fetch the to-do list progress for the employee with
    the specified ID from the RESTful API and display the progress.
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])

    total_count = 0
    completed_count = 0
    completed_list = ''

    user_data = get(user_url).json()
    todo_data = get(todo_url).json()

    for task in todo_data:
        if task.get('completed') is True:
            completed_count += 1
            completed_list += "\t {}\n".format(task.get('title'))
        total_count += 1

    print("Employee {} is done with tasks({}/{}):".format(user_data.get('name'), completed_count, total_count))
    print(completed_list, end="")

