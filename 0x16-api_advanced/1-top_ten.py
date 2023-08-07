#!/usr/bin/python3
"""Work with the reddit api"""

import requests
def top_ten(subreddit):
    """Get the number of subscribes to a the subreddit parameter"""
    headers = {
            'Accept': 'application/json',
            'User-Agent': 'Myapp'
    }
    response = requests.get(
        'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        items = response.json()['data']['children']
        for item in items:
            print(item['data']['title'])
    else:
        print(None)

