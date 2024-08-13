#!/usr/bin/python3
"""
Function that queries Reddit API and prints titles.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                'AppleWebKit/357.36 (KHTML. like Gecko) Chrome/58.0.3029.110'
                'Safari/537.3'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                timeout=20)
        # Check for redirection or invalid subreddit
        if response.status_code == 302:
            print(None)
            return
        # Check if response status code is not 200
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        # Print the titles of the first 10 posts
        for post in posts[:10]:
            print(post['data'].get('title', ''))
    except requests.RequestException:
        # Print None if there is a network or request error
        print(None)
