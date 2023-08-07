#!/usr/bin/python3
"""Work with the reddit api"""

import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribes to a the subreddit parameter"""
    reddit = 'https://www.reddit.com'
    headers = {
            'Accept': 'application/json',
            'User-Agent': 'Myapp'
    }
    response = requests.get(
        '{}/r/{}/about/.json'.format(reddit, subreddit),
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
