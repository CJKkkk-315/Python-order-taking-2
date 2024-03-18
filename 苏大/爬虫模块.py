from bs4 import BeautifulSoup
import requests
reaponse = requests.get("http://scst.suda.edu.cn")
soup = BeautifulSoup(reaponse.text, "lxml")
urls_a = soup.find_all(name='a')
res_url = []
for url_a in urls_a:
    url = url_a.get('href')
    if url and url[:4] != 'http':
        url = 'http://scst.suda.edu.cn' + url
        res_url.append(url)
for i in range(len(res_url)):
    response = requests.get(res_url[i])
    response.encoding = response.apparent_encoding
    content = response.text
    with open('HTMLS\\' + str(i) + '.html','w',encoding='utf-8') as f:
        f.write(content)

