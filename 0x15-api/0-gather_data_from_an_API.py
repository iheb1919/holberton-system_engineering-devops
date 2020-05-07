#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

if __name__ == '__main__':

    try:
        idd = int(sys.argv[1])
    except ValueError:
        print("id must be an integer")

    url = "https://jsonplaceholder.typicode.com/"
    task_done = requests.get(url + "todos?userId={}&completed=true"
                             .format(sys.argv[1]))
    tasks = requests.get(url + 'todos?userId=' + sys.argv[1])
    name = requests.get(url + 'users/' + sys.argv[1]).json()["name"]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(task_done.json()), len(tasks.json())))
    for i in tasks.json():
        if i["completed"]:
            print("\t " + i["title"])
