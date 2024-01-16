#!/usr/bin/python3
"""
Module for task 2
"""
import requests


def recurse(subreddit, after=None):
    """
    Retrieve the top ten posts from a specified subreddit.


    Parameters:
    - subreddit (str): The name of the subreddit to retrieve posts from.

    Returns:
    - None

    Prints the titles of the top ten posts from the specified subreddit
    If the request to the subreddit fails or the subreddit does not
    exist, it prints "None".ders = {"User-Agent": "MyCustomUserAgent/1
    0"}
    """
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
