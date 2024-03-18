import requests
import json
import time
url = "http://ypzsx.gsxt.gov.cn/specialfood_server/milkRecipeNew/queryHealthFood"
keyword = '飞鹤'
payload = '{"currentPage":1,"pageSize":50,"pfcpmc":"' + keyword +'","pfzcbh":"","qymcZw":"","pfspmc":""}'
payload = payload.encode('utf-8')
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;charset=UTF-8',
  'Cookie': '__jsluid_h=542c03dc68f8ccc85103a163bc181119',
  'Origin': 'http://ypzsx.gsxt.gov.cn',
  'Referer': 'http://ypzsx.gsxt.gov.cn/specialfood/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
data = json.loads(response.text)
item_ids = [i['infosharId'] for i in data['data']['list']]
time.sleep(5)
for item_id in item_ids:
    time.sleep(5)
    url = f'http://ypzsx.gsxt.gov.cn/specialfood/#/food/list?id={item_id}&type=yyepf'
    response = requests.get(url)
    print(response.text)
    data = json.loads(response.text)
    print(data['data']['pfcpmc'])
