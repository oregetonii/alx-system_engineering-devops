#!/usr/bin/python3
"""
Function that queris the Reddit API and return number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110'
               'Safari/537.3)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # If the response status code is 302, it indicates a redirect
        if response.status_code == 302:
            return 0
        # If the response status code is not 200, something went wrong
        if response.status_code != 200:
            return 0
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.RequestException:
        # If there is an exception (e.g., network issues), return 0
        return 0
