#!/usr/bin/python3
"""advanced apis"""

import requests


def number_of_subscribers(subreddit):
    """Qureries the Reddit API for the number of subredit.
    Args:
        subreddit: the name of the subreddit
    Returns:
        The number of subscribers(integer) or 0 if the subreddit is invalid
    """
    headers = {"User-Agent": "0x16.api.advanced/v1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        except (KeyError, ValueError):
            return 0
    else:
        return 0
