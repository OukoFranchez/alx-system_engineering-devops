#!/usr/bin/python3

"""
Module for task 2
It requests data from a RESTful API
and returns information about employees tasks
in CSV format
"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


def todo_csv():
    """
    fetches todo list progress of an employee
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
               .format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
               .format(argv[1])

    user_data = get(user_url).json()
    todo_data = get(todo_url).json()

    with open('{}.csv'.format(user_data.get('id')), 'w',
              encoding='utf-8') as tasksData:
        taskwriter = writer(tasksData, quoting=QUOTE_ALL)
        for task in todo_data:
            taskwriter.writerow([user_data.get('id'),
                                 user_data.get('username'),
                                 task.get('completed'),
                                 task.get('title')])

    if __name__ == "__main__":
        todo_csv()
