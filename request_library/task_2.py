import requests

import json

response = requests.get('https://api.pushshift.io/reddit/comment/search/')
data = response.json()
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
