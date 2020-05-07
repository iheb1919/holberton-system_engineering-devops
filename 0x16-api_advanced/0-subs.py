#!/usr/bin/python3
"""
How many subs?
"""

import requests


def number_of_subscribers(subreddit):
    url = 'http://reddit.com/r/{}/about.json'
    header = {'User-agent': 'iheb1919'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
