#!/usr/bin/python3
"""
Function that queries Reddit API and returns a list of titles.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
               'AppleWbKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110'
               'Safari/537.3'}
    params = {}

    if after:
        params['after'] = after

    try:
        response = request.get(url, headers=headers, params=params,
                               allow_redirects=False, timeout=30)
        # Check for redirection or invalid subreddit
        if response.status_code == 302 or response.status_code != 200:
            return None

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        # Add titles of the current page to the hot_list
        for post in posts:
            hot_list.append(post['data'].get('title'))

        # Check if there is a next page
        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    except requests.RequestException:
        # Return None if there is a network or request error
        return None
