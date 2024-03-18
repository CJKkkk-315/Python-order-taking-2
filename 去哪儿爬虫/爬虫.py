import requests
import json
import csv
import time
# 省份信息
pros = """
1	北京市	京
2	天津市	津
3	河北省	冀
4	山西省	晋
5	内蒙古	蒙
6	辽宁省	辽
7	吉林省	吉
8	黑龙江	黑
9	上海市	沪
10	江苏省	苏
11	浙江省	浙
12	安徽省	皖
13	福建省	闽
14	江西省	赣
15	山东省	鲁
16	河南省	豫
17	湖北省	鄂
18	湖南省	湘
19	广东省	粤
20	广西	桂
21	海南省	琼
22	重庆市	渝
23	四川省	川
24	贵州省	黔
25	云南省	滇
26	西藏	藏
27	陕西省	陕
28	甘肃省	甘
29	青海省	青
30	宁夏	宁
31	新疆	新
32	台湾省	台
33	香港	港
34	澳门	澳
"""
# 处理省份信息
pros = [i.split()[1].replace('省','').replace('市','') for i in pros.split('\n') if i]
payload={}
headers = {
    'authority': 'piao.qunar.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'SECKEY_ABVK=AUfAXuVhxZdsXLUlzNYOX+jBus5Kt7fg1fh8F+yviMo%3D; BMAP_SECKEY=AvT9wF0g74V2Y6lhTTgH6IEL5m1dUx9Tged3FHO7MWz91mQF8gKHA_oitW1abfKKU3M-Jgkv8b911WHlA_Gcx-bYG41T1tqINKvBXWuCEcWgcsc1dAFdpLSwYvSk5d64O7RmPH-J2ncIGpthPE_g8E_xdxvh6nWwEwXk71Fn9CJ7ERp-5lKbo0ELQxFtUh7o; QN1=00008d802eb4407c7850dd92; QN300=organic; QN99=2070; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=weCkd8DWqzc29Wyl7YoFRIjB7TC78IgF; _i=VInJOmqoD6pUOypqYqhLV2riSHYq; QN601=9a98101fa4db62811b0762c2d7aac1e6; QN48=00008d802f10407c7a086b0a; quinn=4860de8fc62b970a4a21d3097b76f217af609d4f50e4123cecda580239f39402b5f0ddb803a0ff709cfce4f501055247; fid=642f58a1-2e78-4741-abc6-fdedfda84240; QN205=organic; QN277=organic; QN57=16552115726200.9617809314879928; QN269=D544D633EBE111EC9DA1FA163E52BE3B; Hm_lvt_15577700f8ecddb1a927813c81166ade=1655211573; QN63=%E4%B8%AD%E5%9B%BD; QN267=0623206714b7ccd54e; _vi=oOKj6uvUXIDGQR-cy3WRH5p4QhbqynkQeRXo0Ersw0_6eaTgMNrN89q2OpPHeUCcq2HxONOVWNhMBLxr3f9TTHvA1bkFSn2E0bkMQ2q0XQ52EAIHlKUjxhrA5BlhICIdj5Ek--VghyJWd84SsUXtyQwL38j6lrf3-VXSWKP0U_4i; ariaDefaultTheme=undefined; QN58=1655215083744%7C1655215083744%7C1; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1655215084; QN271=97f63a81-e3d9-4632-a36d-7fdd0daa68e3; __qt=v1%7CVTJGc2RHVmtYMTlsY0tCclB1NzV2NzAxVVk3SUl6Q0hKcTBoRjBBc0tOWmk1U0lnVXY0b0NzUWdEVlU4bUpnQVVvbmtCYytReEZDV1VQQXkyYTNKdGFMamlta09vL2NwT2YvQ05qSVExWlRELytuQVZxRWxaYVc3emVXMlFVWXdGTHNJbGkwZjhmNkNZWFJ3NFEzOVJLdWFiV3R0VWxpSGNJL0dQYXBMUm5zPQ%3D%3D%7C1655215090674%7CVTJGc2RHVmtYMTlpWVJhem82ZlBPS1RTV2I2NDcxT2VQVmQ0ZFR0RExJdEF3ampXRVpoNEdoNkRsUFZxSk1ZY1RQdXlUVm5IdDJDbThoRUdOeHNFQVE9PQ%3D%3D%7CVTJGc2RHVmtYMS9IY01mMlh4bTdsdWJtVzNaV1AzcERNT1EvdzB0OGVvZTZnV1ZENEc5RENtZTN2WlVuU2lnQ0ZsSFJFWnVFRnVYN0lQbENRb2FWZVl5UEpJM0I3WkpGZkllc2ZhSGl6Tm5IYTRYVkRiU3Ria280QytHZTl2MnRxVHgvcW1hcnNYNDM2ZTUzajNzY3N5OXFUS0R6bUNJVnlPZU1lUHU1TmdSaDBXZDJtNXZIaktpS0pvUEdVUkkvaDd0d1BKU3Z3QnpqZEF4eXlnc3d0M29UZ1ZBQW9ZbWFZb1Y4a1lJclV2L0t1bWk2MkgxQ3YxWGVyWUQ4d29FbmRRRzNmanFEOGYyZU5zTGFyZVNZdGY2eWk4ekJrK3pndTlzQm9IQi95aTQ5SVNvazh0aWhoajhxS09lZnQ0SVRpdThIYkxCRGlPVTJaTFdqcjQ4ekZvZFV1NVZwaHpBa1VGVEVIK0xTakZsanNDeG8rblpOSWg0THI5cXBaTGxpMXVhL2tza2VJRFpYcThxcHZSeXhBQ0RMSFFEZEgrMW9VQlBLREgwaDczMTBvVXNWQ2ZzdlhmaThYL0RXZVdOdmR0a1g2c2ZiU1FpNSs1RFpCcy9vRDZoWHVmeDhjTEkyblhhbVBrZzNhNFJKTFNBek5raDJodVJoSDN1TXVFUlRMdGRXbU5QejZKTGJhOFM2WWZ4cTBDdzJTT1NzVjQ3RDNNS1J0R0RFYkNMY2RTS1pONVoweFBzZUFDcnkxTHQ1ekd3bFlyWTdBajNSSE02ajEzeVY4WVVBV1hHM1hnc0pkdUJrQnNxTFNGR0hIU1djblkxc290OWRhMTB1VVJIaFl4Szd1aHlwK3FMSnlsUk1XcC92TTZtR3cwbVA4enNYRDBtWlEzZ2JHa1pSQjVJTk1uTk80VGJoTWwyZnZQWkROelB1ajhqRTFCcmY5cUtCaVkxK0tUSENnbWp0dXdOYnU4ZkJQZ3Z5UHp0MXVKNUFodjczbTNOR2xOYXpXbFdtTHZvcEhOK2lZT25oUlBvb3lQNnBmUzM4eXlJT284R1RVVWxNSjNCMURZMXRYOUVPQU1iK2JxQlNJY3VUT1lmaw%3D%3D; JSESSIONID=8CA557FA18E4C70BD6EB11A7C8AA47A0; JSESSIONID=4C83340586839E9F027EDADB38059479',
    'referer': 'https://piao.qunar.com/ticket/list.htm?keyword=%E4%B8%AD%E5%9B%BD&region=&from=mpl_search_suggest&page=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
    'x-requested-with': 'XMLHttpRequest'
}
# 打开csv文件
f = open('res.csv','a+',newline='',encoding='utf-8')
fcsv = csv.writer(f)
# 依次爬取每个省份数据
for pro in pros:
    for page in range(1,11):
        time.sleep(1)
        print(page)
        url = f"https://piao.qunar.com/ticket/list.json?keyword={pro}&region=&from=mpl_search_suggest&page=" + str(page)
        response = requests.request("GET", url, headers=headers, data=payload)
        js = json.loads(response.text)
        # 提取其中的景点数据
        for i in js['data']['sightList']:
            # 将自己需要的数据写入csv中
            try:
                print(i)
                row = [i['sightName'],i['address'],i['star'],i['score'],i['qunarPrice'],i['saleCount']]
                fcsv.writerow(row)
            except:
                continue
f.close()
