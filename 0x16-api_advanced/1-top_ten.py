#!/usr/bin/python3
"""
Top Ten
"""

import requests


def top_ten(subreddit):
    url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'iheb1919'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code != 200:
        print('None')
        return
    else:
        data = r.json()['data']
        children = data.get('children')
        i = 0
        for hot in children:
            if (i < 10):
                print(hot.get('data').get('title'))
                i += 1
