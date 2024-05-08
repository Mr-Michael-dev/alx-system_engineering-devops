#!/usr/bin/python3
"""
 function that queries the Reddit API and prints
 the title of top 10 hot posts
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"

    headers = {'User-Agent': 'ubuntu:apiProject/v1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        hot_posts_titles = []
        for post in posts:
            post_data = post['data']
            hot_posts_titles.append(post_data['title'])
        for title in hot_posts_titles:
            print(f"{title}")
    else:
        print('None')
