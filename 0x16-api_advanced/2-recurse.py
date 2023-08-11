#!/usr/bin/python3
"""Work with the reddit api"""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''Get posts from a subreddit'''
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'MyApp'
    }
    sort = 'hot'
    limit = 30
    response = requests.get(
            '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
                'https://www.reddit.com',
                subreddit,
                sort,
                limit,
                n,
                after if after else ''
            ),
            headers=headers,
            allow_redirects=False
    )
    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
