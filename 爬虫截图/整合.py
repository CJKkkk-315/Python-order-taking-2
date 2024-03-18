import requests

res = requests.get('https://39.103.237.89:8090',verify=False)
print(res.text)