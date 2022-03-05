import concurrent.futures
import json
import requests


def subreddit_url():
    sub_url = ['car', 'bmw']
    urls = []
    for sub in sub_url:
        url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={sub}"
        urls.append(url)
    return urls


def get_subreddit_comment(url):
    response = requests.get(url)
    if response.ok:
        data = response.json()
        with open('data_file.json', 'w') as f:
            json.dump(data, f, indent=4)


def main():
    with concurrent.futures.ProcessPoolExecutor() as pool:
        data = []
        for url in subreddit_url():
            rez = pool.submit(get_subreddit_comment, url)
            data.append(rez)


if __name__ == '__main__':
    main()
