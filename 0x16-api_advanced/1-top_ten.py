#!/usr/bin/python3
"""advanced apis"""
import requests


def top_ten(subreddit):
    """Qureries the Reddit API for the number of subredit.
    Args:
        subreddit: the name of the subreddit
    Returns:
        prints the top ten
    """
    headers = {"User-Agent": "0x16.api.advanced/v1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    data = response.json().get("data")
    [print(val.get("data").get("title")) for val in data.get("children")]
