#!/usr/bin/python3
"""Work with the reddit api"""

import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribes to a the subreddit parameter"""
    reddit = 'https://www.reddit.com'
    headers = {
            'Accept': 'application/json',
            'User-Agent': ' '.join([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'AppleWebKit/537.36 (KHTML, like Gecko)',
                'Chrome/97.0.4692.71',
                'Safari/537.36',
                'Edg/97.0.1072.62'
            ])
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
