# ~*~ coding: utf-8 ~*~
from gevent.lock import BoundedSemaphore
sem = BoundedSemaphore(1)

import requests
import random
import time
from functools import wraps

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

BAIDU_HEADERS = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.baidu.com',
}


class Proxies:
    current_proxies = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Proxies, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def set_current_proxies(self, proxy_ip):
        self.current_proxies = proxy_ip

    def get_current_proxies(self):
        return self.current_proxies

    def has_exist_current_proxies(self):
        if self.current_proxies:
            return True
        return False

    def disable_current_proxies(self):
        self.set_current_proxies(None)

    @staticmethod
    def get_by_kdl(ssl):
        username = "1409131536"
        password = "qdpmki4i"
        api_url = "http://dps.kdlapi.com/api/getdps/?orderid=944671907449151&num=1&pt=1&format=json&sep=1"

        content = requests.get(api_url).json()
        print(content)
        if content.get('code') == 0:
            proxy_ip = content['data']['proxy_list'][0]
            proxies = {
                "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                "proxy": proxy_ip},
                "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                 "proxy": proxy_ip}
            }
            return proxies
        else:
            print({'data': '无代理可用', 'is_success': 0})
            quit("无代理可用")

    def get_proxies(self, ssl=False):
        """ 获取代理ip地址 """
        if self.has_exist_current_proxies():
            proxies = self.get_current_proxies()
        else:
            proxies = self.get_by_kdl(ssl)
            self.set_current_proxies(proxies)
            print('当前的IP是：{}'.format(proxies.__str__()))
        return proxies


def get_proxies_instance():
    proxies = Proxies()
    return proxies


def enable_proxies(ssl=False):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            while True:
                try:
                    sem.acquire()
                    proxy_ip = get_proxies_instance().get_proxies(ssl)
                    sem.release()
                    headers = {
                        'User-Agent': random.choice(USER_AGENTS)
                    }
                    result = func(proxies=proxy_ip, headers=headers, *args, **kwargs)
                    break
                except Exception as e:
                    print(e)
                    get_proxies_instance().disable_current_proxies()
                    time.sleep(3)
            return result
        return inner
    return outer


def disable_proxies():
    get_proxies_instance().disable_current_proxies()


@enable_proxies(ssl=False)
def get(url, params=None, proxies=None, headers=None, cookies={}, timeout=10, **kwargs):
    if kwargs.get('change_headers'):
        headers.update(BAIDU_HEADERS)
    return requests.get(url, params=params, proxies=proxies, headers=headers,
                        cookies=cookies, timeout=timeout, verify=False)


class MyGet:
    def __init__(self):
        temp_cookies = 'BIDUPSID=03F08D61C96B8A46D347EB8F32AC8BDF; PSTM=1523424203; BAIDUID=1A1599F7CD3D187A2548BE3FA37C6381:FG=1; H_WISE_SIDS=107315_110085_127969_128699_131423_144966_154213_156287_156926_162898_163275_163566_163808_164164_164297_164848_164992_165071_165136_165143_165328_166147_166256_166474_166941_167085_167292_167295_167303_167403_167435_167538_168095_168315_168398_168403_168564_168570_168615_168631; __yjs_duid=1_7841fec4ca6146cdacbeaed5b376fa201619688182892; BDUSS=C1PSDdiRkRycWdSSjZzWkplcHBHZDlNOUF1OWpkNTBUQnJDZERwb2F0S1QzR2hoSVFBQUFBJCQAAAAAAAAAAAEAAABK8tM0ueLXxcaoucnPubnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNPQWGTT0Fhb; BDUSS_BFESS=C1PSDdiRkRycWdSSjZzWkplcHBHZDlNOUF1OWpkNTBUQnJDZERwb2F0S1QzR2hoSVFBQUFBJCQAAAAAAAAAAAEAAABK8tM0ueLXxcaoucnPubnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNPQWGTT0Fhb; Hm_lvt_4fd9c3ab38c6c37110df1ff930ba679a=1637111339; Hm_lpvt_4fd9c3ab38c6c37110df1ff930ba679a=1637111339; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=GSLOJexroG0vo9rHkrz-tOU1E2KKg7jTDYrEOwXPsp3LGJLVgXVTEG0Pt8dKPFPbDINlogKKWmOTH7kF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJFJoC-MJDI3H48k-4QEbbQH-UnLqM6NWmOZ04n-ah02fRcLMx7Oqt3L5-nPJxLHW23M_bcm3UTKsq76Wh35K5tTQP6rLt-e2CO4KKJxbp52sprsBP5ZQnIihUJiBhbLBan7_bvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbCDwe50-j6vQeU5eetjK2CntsJOOaCv48pTOy4oWK441DhjyqRj72-jT5tbvQCjphlvobTJ83M04K4o9-hvT-54e2p3FBUQJoMQ2Qft20b3bb-RT0qOa3g5wWn7jWhvRDq72y5JOQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDq6kjJJFOoIv5b-0_qJOnq4bohjPFM-v9BtQO-DOxoPQOf4o1jTC9jbOc3j_kD4RiK5bBQgnkQq5Y2IbBMf7Tj4O_ypKsWbjn0x-jLTPO0pvx3fJDshT8h-nJyUPihtnnBTbW3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfCP2MCL9D5RDKICV-frb-C62aKDsbxQnBhcqJ-ovQT3-hTFXyM4LqU5JBaIDKCocWb0bjxbeWJ5pXn-R0hbjJM7xWeJp0MnCQp5nhMJme-Ov0MKr-4OAWt7y523i-b6vQpPbjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjcbDaDqqT8sKjAX3JjV5PK_Hn7zeUJ6XM4pbq7H2M-jbD88Qqno-tFVfh7aDf_KyUPsjU6n0pcH3mOfhUJb-IOdspcs34Ji3l0kQN3T-TvbWaRlbnogWlrSDn3oypJVXp0njURly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJUutfD7H3KC-tCIaMf5; delPer=0; PSINO=6; BAIDUID_BFESS=1A1599F7CD3D187A2548BE3FA37C6381:FG=1; BDSFRCVID_BFESS=GSLOJexroG0vo9rHkrz-tOU1E2KKg7jTDYrEOwXPsp3LGJLVgXVTEG0Pt8dKPFPbDINlogKKWmOTH7kF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJFJoC-MJDI3H48k-4QEbbQH-UnLqM6NWmOZ04n-ah02fRcLMx7Oqt3L5-nPJxLHW23M_bcm3UTKsq76Wh35K5tTQP6rLt-e2CO4KKJxbp52sprsBP5ZQnIihUJiBhbLBan7_bvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbCDwe50-j6vQeU5eetjK2CntsJOOaCv48pTOy4oWK441DhjyqRj72-jT5tbvQCjphlvobTJ83M04K4o9-hvT-54e2p3FBUQJoMQ2Qft20b3bb-RT0qOa3g5wWn7jWhvRDq72y5JOQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDq6kjJJFOoIv5b-0_qJOnq4bohjPFM-v9BtQO-DOxoPQOf4o1jTC9jbOc3j_kD4RiK5bBQgnkQq5Y2IbBMf7Tj4O_ypKsWbjn0x-jLTPO0pvx3fJDshT8h-nJyUPihtnnBTbW3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfCP2MCL9D5RDKICV-frb-C62aKDsbxQnBhcqJ-ovQT3-hTFXyM4LqU5JBaIDKCocWb0bjxbeWJ5pXn-R0hbjJM7xWeJp0MnCQp5nhMJme-Ov0MKr-4OAWt7y523i-b6vQpPbjpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjcbDaDqqT8sKjAX3JjV5PK_Hn7zeUJ6XM4pbq7H2M-jbD88Qqno-tFVfh7aDf_KyUPsjU6n0pcH3mOfhUJb-IOdspcs34Ji3l0kQN3T-TvbWaRlbnogWlrSDn3oypJVXp0njURly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJUutfD7H3KC-tCIaMf5; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1639733455,1639971931,1640145304,1640164816; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BA_HECTOR=0gak2084a00l008kk71gs7jo80q; BDRCVFR[C0p6oIjvx-c]=ddONZc2bo5mfAF9pywdpAqVuNqsus; H_PS_PSSID=34442_35105_35240_35489_35436_35457_34584_35491_34578_34873_35234_35320_35478_35562; ZD_ENTRY=empty; session_id=16402224844465244701034323989; shitong_key_id=2; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1640222513; ab_sr=1.0.1_Y2E5MTUwZWUxY2NmMTBjZjQ3YjE1M2Y4MmIyOTQzOWQ2YzJlZmQzZWIxNmE5Zjc4N2Q3YWJhNzU4MWMxOGQ3OWVkNTliM2UwZWMxMDA3MmQ3MzJhODNmNzNlZjY3ZTRlZTZjOTBjOWEwMjRjZDI1MGMxZmQzYmM3ODIzZTJjYWRjOWFlZDI3ZDMwZWM0ZDU4ZjY5OWI2NGE3YzJlNDIxOWQ5ZTViNTk5YjcwMmU4ZDMyYTFmODU4ODRiNGY4MmEz; shitong_data=d45d7c53f693057bfc9b91aeec6acf39c3c4409677a2cd6da25ca7b234724d127e50b4dc8fcec2ee28692b24554290d1e58abd28b413a5a35892dba1bd8cac0c3644bc0c8daf30ad06e43b1eae0927f8182a0c12c99b3fd7bd038987609feee803015554c599f37fe73bf397c0857cd8b50693e0d46501caced021359e5a5898; shitong_sign=3478ac3e'
        self.zd_cookies = {}
        for ii in temp_cookies.split(';'):
            value = ii.split('=')
            self.zd_cookies[value[0]] = value[1]

    def get_baidu(self, url, change_proxies):
        if change_proxies:
            print('触发 - Disable Proxies')
            disable_proxies()

        while True:
            response = get(url, change_headers=True)
            if response.status_code != 200:
                continue
            if response.text.find("此验证码用于确认这些") != -1:
                print("验证码检测")
                continue
            if response.text.find("百度安全验证") != -1:
                print("百度安全验证")
                continue
            break
        return response

    def get(self, url):
        while True:
            response = get(url, cookies=self.zd_cookies)

            if response.status_code != 200:
                continue

            if response.text.find("此验证码用于确认这些") != -1:
                print("验证码检测")
                continue
            break

        return response
