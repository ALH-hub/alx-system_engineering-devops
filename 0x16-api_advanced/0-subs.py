#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given Reddit subreddit.

This script utilizes the Requests library to make an HTTP GET request to the
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a Reddit subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit, or 0 if not found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
      "User-Agent": "MyRedditSubscriberCounter/v1.0 (by u/Complete-Visual894)"
      }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        return 0
