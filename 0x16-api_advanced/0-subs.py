#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """function that returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my_bot/0.1"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception as e:
        return 0


if __name__ == "__main__":
    subreddit_name = "programming"
    subscribers_count = number_of_subscribers(subreddit_name)
    print(subscribers_count)
