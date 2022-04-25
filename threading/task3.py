import concurrent.futures
import json
import requests


def subreddit_url():
    sub_url = [ 'pharm','chemistry','scient']
    urls = []
    for sub in sub_url:
        url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={sub}"
        urls.append(url)
    return urls


def name_file():
    i = 1
    while True:
        yield f'data_{i}.json'
        i += 1


def get_name_file():
    g = name_file()
    def myfunc():
        return next(g)
    return myfunc


get_file_name = get_name_file()


def get_subreddit_comment(url, filename):
    response = requests.get(url)
    if response.ok:
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)


with concurrent.futures.ThreadPoolExecutor(3) as executor:
    data = []
    for url in subreddit_url():
        data.append(executor.submit(get_subreddit_comment, url, get_file_name()))
    for thread in concurrent.futures.as_completed(data):
        data.append(thread.result())

