#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'ubuntu:apiProject/v1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']['children']
        return data[0]['data']['subreddit_subscribers']
    else:
        return 0
