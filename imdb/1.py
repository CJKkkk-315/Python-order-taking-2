import requests
import json
key = 'k_2q8wl6a7'
def do1():
    movie = input('请输入你要查询的电影：')
    url = f'https://imdb-api.com/zh/API/SearchMovie/{key}/{movie}'
    res = requests.get(url)
    data = json.loads(res.text)['results'][0]
    mid = data['id']
    title = data['title']
    url = f'https://imdb-api.com/zh/API/Title/{key}/{mid}'
    res = requests.get(url)
    data = json.loads(res.text)
    countries = data['countries']
    imDbRating = data['imDbRating']
    imDbRatingVotes = data['imDbRatingVotes']
    languages = data['languages']
    directors = data['directors']
    print('电影名:', title)
    print('国家:', countries)
    print('评分:', imDbRating)
    print('投票人数:', imDbRatingVotes)
    print('语种:', languages)
    print('导演:',directors)
def do2():
    num = int(input('请输入要展示的电影数量(最大250):'))
    url = f'https://imdb-api.com/zh/API/Top250Movies/{key}'
    res = requests.get(url)
    data = json.loads(res.text)['items']

    movies = []
    for j in data:
        movies.append([j['title'],j['year'],j['imDbRating']])
    movies = movies[:num]
    for movie in movies:
        print("电影名：{:<60} 年份：{:<60} 评分：{:<60}".format(movie[0], movie[1], movie[2]))
def do3():
    movie = input('请输入你要查询的电影：')
    url = f'https://imdb-api.com/zh/API/SearchMovie/{key}/{movie}'
    res = requests.get(url)
    data = json.loads(res.text)['results'][0]
    mid = data['id']
    url = f'https://imdb-api.com/en/API/Posters/{key}/{mid}'
    res = requests.get(url)
    url = json.loads(res.text)['posters'][0]['link']
    r = requests.get(url)
    with open(f'{movie}.jpg', 'wb') as f:
        f.write(r.content)
    print('下载成功！')
info = """

    欢迎来到电影查询系统

1.查询电影具体信息
2.展示TOP250电影排行
3.下载电影海报
4.退出

"""
while True:
    print(info)
    c = input('请输入你的选择：')
    if c == '1':
        do1()
    elif c == '2':
        do2()
    elif c == '3':
        do3()
    elif c == '4':
        break
    else:
        print('输入错误，请重试')