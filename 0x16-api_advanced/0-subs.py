#!/usr/bin/python3
"""
Reddit API
"""
import json
import requests
"""
queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Ons_sheckler"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0

# 1 enter the url on my browser 'https://www.reddit.com/r/programming/.json'
# 2 press f12 / inspect element and refresh page
# 3 go to network - all
# 4 copy as cURL
# 5 paste in https://curl.trillworks.com/ a curl converter to python request
# 6 look for the header ' User-Agent'
# 7 the json request have 2 keys Data and Kind
# 8 look for 'subscribers' in the 'Data' list

#for more information: https://www.youtube.com/watch?v=Mw-dsY8UKVs
