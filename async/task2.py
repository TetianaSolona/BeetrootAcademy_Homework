import json
import requests
import asyncio

def subreddit_url():
    sub_url = ['country', 'Ukraine', 'freedom']
    urls = []
    for sub in sub_url:
        url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={sub}"
        urls.append(url)
    return urls


async def get_subreddit_comment(url):
    response = requests.get(url)
    if response.ok:
        data = response.json()
        with open('data_file.json', 'w') as f:
            json.dump(data, f, indent=4)

urls = subreddit_url()

async def main():
    for u in urls:
        await asyncio.create_task(get_subreddit_comment(u))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
