import requests
import json
import sys

response = requests.get('https://itunes.apple.com/lookup?id=' + sys.argv[1])
x = response.json()
print(json.dumps(x, indent=4))