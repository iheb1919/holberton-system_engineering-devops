#!/usr/bin/python3
"""
Export to CSV
"""

import csv
import requests
import sys

if __name__ == '__main__':

    try:
        idd = int(sys.argv[1])
    except ValueError:
        print("id must be an integer")

    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/" + sys.argv[1])
    task = requests.get(url + "todos",
                        params={"userId": sys.argv[1]})
    username = user.json()["username"]

    with open(sys.argv[1] + ".csv", "w", newline='') as csvf:
        prin = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for i in task.json():
            prin.writerow([i["userId"], username, i["completed"],
                           i["title"]])
