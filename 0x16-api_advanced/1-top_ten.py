#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my_bot/0.1"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            children = data["data"]["children"]
            if not children:
                print("No hot posts found.")
            else:
                for i, child in enumerate(children[:10]):
                    print(f"{i + 1}: {child['data']['title']}")
        else:
            print("None")
    except Exception as e:
        print("None")


if __name__ == "__main__":
    subreddit_name = "programming"
    top_ten(subreddit_name)
