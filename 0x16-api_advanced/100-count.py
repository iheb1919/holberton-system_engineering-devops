#!/usr/bin/python3
"""
Recurse it!
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
    url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'iheb1919'}
    req = requests.get(url.format(subreddit), headers=header,
                       params={'t': all, 'after': after})
    if not req or req.status_code != 200:
        return None
    for i in req.json()['data']['children']:
        hot_list.append(i['data']['title'])
    after = req.json().get('data').get('after')
    if after:
        count_words(subreddit, word_list, hot_list, after)
    return hot_list
