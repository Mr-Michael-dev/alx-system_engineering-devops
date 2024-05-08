#!/usr/bin/python3
"""
 function that queries the Reddit API and returns
 the title of top all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'ubuntu:apiProject/v1'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            post_data = post['data']
            hot_list.append(post_data['title'])

        # Check if there are more posts to fetch
        after = data['data'].get('after')
        if after:
            # Recursively call the function with the 'after' parameter
            recurse(subreddit, hot_list, after)
        else:
            # If there are no more posts, return the hot_list
            return hot_list
    else:
        # If the subreddit is invalid, return None
        return None
