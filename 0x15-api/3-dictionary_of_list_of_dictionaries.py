#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""

import json
import requests
import sys
from collections import OrderedDict

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/")
    task = requests.get(url + "todos")
    json0 = {}
    for i in user.json():
        json1 = []
        json2 = {}
        for j in task.json():
            if i["id"] == j["userId"]:
                json2.setdefault("username", i["name"])
                json2.setdefault("task", j["title"])
                json2.setdefault("completed", j["completed"])
                json1.append(json2)
                json0.setdefault(i["id"], json1)
    with open("todo_all_employees.json", "w", newline="") as fcsv:
        json.dump(json0, fcsv)
