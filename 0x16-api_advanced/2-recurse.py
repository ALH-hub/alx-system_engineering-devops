#!/usr/bin/python3
"""advanced apis"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Qureries the Reddit API for the number of subredit.
    Args:
        subreddit: the name of the subreddit
    Returns:
        prints the top ten
    """
    headers = {"User-Agent": "0x16.api.advanced/v1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for i in data.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    print(hot_list)

    return hot_list
