#!/usr/bin/python3
"""
Recurse it!
"""

import requests



def recurse(subreddit, hot_list=[], after=""):
    url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'iheb1919'}
    params = {'t': all, 'after': after}
    req = requests.get(url.format(subreddit), headers=header,
                       params=params)
    print(url.format(subreddit), headers=header,
                       params=params)
    if req.status_code != 200 or not req:
        return None
    for i in req.json()['data']['children']:
        hot_list.append(i['data']['title'])
    after = req.json().get('data').get('after')
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
