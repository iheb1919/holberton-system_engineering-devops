#!/usr/bin/python3
"""
"""
import requests
import sys

if __name__ == '__main__':

    try:
        idd = int(sys.argv[1])
    except ValueError:
        print("id must be an integer")

    url = "https://jsonplaceholder.typicode.com/"
    task_done = requests.get(url + 'todos',
                             params={"userId": sys.argv[1]}).json()
    tasks = requests.get(url + 'todos?userId=' + sys.argv[1]).json()
    name = requests.get(url + 'users/' + sys.argv[1]).json()["name"]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(task_done), len(tasks)))
    for i in tasks:
        if i["completed"]:
            print("\t " + i["title"])
