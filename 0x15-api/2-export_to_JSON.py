#!/usr/bin/python3
"""
Export to JSON
"""

import json
import requests
import sys
from collections import OrderedDict

if __name__ == '__main__':

    try:
        idd = int(sys.argv[1])
    except ValueError:
        print("id must be an integer")
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1])
    task = requests.get(url + "todos",
                        params={"userId": sys.argv[1]})
    json0 = {}
    json1 = []
    for i in task.json():
        json2 = {}
        json2.setdefault("task", i["title"])
        json2.setdefault("completed", i["completed"])
        json2.setdefault("username", user.json()["name"])
        json1.append(json2)
    json0.setdefault(sys.argv[1], json1)
    with open(sys.argv[1] + ".json", "w") as fcsv:
        json.dump(json0, fcsv)
