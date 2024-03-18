headers = {
  'authority': 'www.guazi.com',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Opera";v="84"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'referer': 'https://www.guazi.com/buy',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': 'platform=pc; cityId=158; cityDomain=changzhi; cityName=%E9%95%BF%E6%B2%BB; uuid=c1e221f1-1f6b-494c-90e5-a0e4a8083e82; sessionid=17a78f54-161a-49c1-c477-4994c4fb2a44; cainfo=%7B%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22c1e221f1-1f6b-494c-90e5-a0e4a8083e82%22%7D; ca_s=self; ca_n=self; SECKEY_ABVK=ZTfdvCcZD9fkzka/rB/3FYA1OHW1DyxE/BuHCaeoBYA%3D; BMAP_SECKEY=uItVsDqVyi9uLwIq1--KE0q6zs0-a9x2f6hBaLhmOKkDUkoBaOftCy5Ie_atxfZ19j5twvBhF1WJt-hEu11dE4iTfNc8mej-SuCYIXRPGlS8lB-gcXbVPYt7ATkIywI_qqHe5gUvK55V1AoPF_txasu2kPmbxoWckQ8QMJP_gNZqVUu3jByGeldT1pTHI7Zu; cityId=158; cityDomain=changzhi; cityName=%E9%95%BF%E6%B2%BB'
}
response = requests.get('https://www.guazi.com/Detail?clueId=117062458',headers=headers)
soup = BeautifulSoup(response.text)
print(soup.find(class_='price-main').find(name='span').text)