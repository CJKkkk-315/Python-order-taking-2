# coding=utf-8
import requests


def tes():
    username = "1409131536"
    password = "qdpmki4i"
    api_url = "http://dps.kdlapi.com/api/getdps/?orderid=944006805600959&num=1&pt=1&format=json&sep=1"
    content = requests.get(api_url).json()
    if content.get('code') == 0:
        proxy_ip_list = content['data']['proxy_list']
        for proxy_ip in proxy_ip_list:
            proxies = {
                "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                "proxy": proxy_ip},
                "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                 "proxy": proxy_ip}
            }
            print(proxies)
            # headers = {
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            #     'Host': 'www.baidu.com',
            # }
            headers = {
                'Connection': 'Keep-Alive',
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Host': 'www.baidu.com',
            }
            # t_cookies = 'BIDUPSID=E53AD60C663D0F33E13E8DA49D3FFD47; PSTM=1639822827; BAIDUID=E53AD60C663D0F33CCF6ED6B00E43DF0:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_669982b352e029fb0ac9f77ebb8016331639828968372; H_WISE_SIDS=107311_110085_127969_164870_179348_181589_184009_184286_185632_185650_186635_186841_187282_187432_187449_187726_188134_188333_188453_188468_188552_188874_189256_189711_189731_189755_190033_190247_190473_190680_190684_190802_191068_191369_191432_191810_192018_192206_192351_192407_193557_193761_194085_194130_194514_194519_194583_194923_194987_195150_195172_195343_195477_195533_195545_195552_195591_195605_195679_195838_195904_195911_195929_196000_196049_196230_196274_196276_196383_196426_196432_196590_196753_196867_196902_196939_197026_197215_197224_197284_197291_197662_197782_197841_198022_198034_198040_198167_198253_8000061_8000127_8000138_8000150_8000164_8000166_8000173_8000182; BDSFRCVID_BFESS=kFtOJeC62AM0SL7HkiZZ--ABamgAg36TH6aoybwRWSVcHj4QFQstEG0PoM8g0KAbnhfQogKKKgOTHI_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JJkO_D_atKvDqTrP-trf5DCShUFsKx6iB2Q-XPoO3KtMqMJCy-4byxQDqtQG54riW5cpoMbgylRp8P3y0bb2DUA1y4vpK-ogQgTxoUJ2fnRJEUcGqj5Ah--ebPRiB-b9QgbAMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0MC09j6KhDTPVKgTa54cbb4o2WbCQ54bv8pcN2b5oQTO3Kb3qBPPfWj-LsljPKR6vOPQKDpOUWfAkXpJvQnJjt2JxaqRC5bj6Sh5jDh3Me-AsLn6te6jzaIvy0hvcWb3cShnVBUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhjGtOtjDttb32WnTJ25rHDbTw5tI_-P4DeN7aBxRZ56bHWh0MJPJmflncjU6WqDuFLxQLBMnqQJ7nKUT13lT_qxJDQ67-Q5FP3xJKQh343bRTLIns5hOAfjC4W4vJhP-UyPRMWh37WGOlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafD_WbDD6ej-Wentebl8XKtQX555tWtOO5t-_HnurMhjOXUI8LNDH3xujL2tfanvV2lKVKqjt-tcJLtbyjRO7ttoyMCrfbf3RQJO1jCbhQlQ55ML1Db3yW6vMtg3C3JrS5fjoepvoyPJc3MkPBPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtJ-8oC0XtKP3qn7I5KTtbtCs2qoXb-RhbPo2WDvo3tbcOR5Jj65NXj89XaJ7a-czytDL5loqaR3NeI8C3MA--t4--lJNLhJpK2bB_UjIL4OMsq0x0-nYe-bQyPQa2tvhLCOMahvc5h7xOhT3QlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J6_ftb7P; BDUSS=WlkSmx-QklpTTUwVXprbU5Ma3NVYnpkUGJObzc0OWVDTE9ncklZTWRSQkluT3BoSUFBQUFBJCQAAAAAAAAAAAEAAAAlT2wiYWFhNjUyNjg2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgPw2FID8Nha; BDUSS_BFESS=WlkSmx-QklpTTUwVXprbU5Ma3NVYnpkUGJObzc0OWVDTE9ncklZTWRSQkluT3BoSUFBQUFBJCQAAAAAAAAAAAEAAAAlT2wiYWFhNjUyNjg2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgPw2FID8Nha; delPer=0; BD_CK_SAM=1; PSINO=5; H_PS_PSSID=35411_34442_35466_35105_31253_35489_35456_34584_35491_35245_35541_35234_35324_26350; sug=3; sugstore=1; ORIGIN=2; bdime=0; H_PS_645EC=cc86cRMKy8Q2OY8Jyf36Z%2BpiBxyQ7vcBwO8v2nzPW00E7XOWvqoff9jKEH0; BA_HECTOR=200g858g0h0h21a4ql1gs89d10r; BDSVRTM=189; WWW_ST=1640244845631'
            # cookies = {}
            # for c in t_cookies.split(';'):
            #     value = c.split('=')
            #     cookies[value[0]] = value[1]
            response = requests.get(url='https://ip.tool.lu/', proxies=proxies)
            print(response.text)
            print("*" * 100)
            response = requests.get(url='https://www.baidu.com/s?wd=江书记现在怎么样了', proxies=proxies, headers=headers)
            print(response.status_code)
            print(response.text)
            print(response.content)


def tes2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Host': 'www.baidu.com',
    }
    response = requests.get(url='https://ip.tool.lu/')
    print(response.text)
    print("*"*100)
    response = requests.get(url='https://www.baidu.com/s?wd=江书记现在怎么样了',  headers=headers)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    tes()
