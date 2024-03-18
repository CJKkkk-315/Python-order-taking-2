import requests
import json
import re
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
# response = requests.get('https://api.openreview.net/notes?content.venue=ICLR+2022+Oral&details=replyCount&offset=0&limit=60&invitation=ICLR.cc%2F2022%2FConference%2F-%2FBlind_Submission',headers=headers)
# data = json.loads(response.text)
# for i in data['notes']:
#         for j in i['content']['authorids']:
#                 print(i['id'],end=' ')
#                 print(j)
response = requests.get('https://openreview.net/profile?id=~António_Farinhas1',headers=headers)
print(response.text)
html_data = re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response.text)[0]
print(json.loads(html_data))