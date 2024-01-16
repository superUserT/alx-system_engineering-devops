#!/usr/bin/python3
import requests

headers = {"User-Agent": "my_bot/0.1"}


def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            children = data["data"]["children"]
            if not children:
                if not hot_list:
                    return None
                else:
                    return hot_list
            else:
                for child in children:
                    hot_list.append(child["data"]["title"])
                after = data["data"]["after"]
                return recurse(subreddit, hot_list, after)
        else:
            return None
    except Exception as e:
        return None


if __name__ == "__main__":
    result = recurse("programming")
    if result is not None:
        print(len(result))
    else:
        print("None")
