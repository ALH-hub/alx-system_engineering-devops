#!/usr/bin/python3
"""advanced apis"""
from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API returns the number of subscribers.
    Parameters:
        subreddit (str): subreddit concerned
    Returns:
        number of subscribers if subreddit found, 0 otherwise
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'MyRedditSubscriberCounter Version 1.0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
