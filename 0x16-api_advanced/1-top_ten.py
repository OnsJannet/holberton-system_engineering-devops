#!/usr/bin/python3
"""
Reddit API
"""
import json
import requests
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    user = {"User-Agent": "Ons_sheckler"}
    request = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        for posts in request.json().get("data").get("children"):
            print(posts.get("data").get("title"))
    else:
        print("None")
