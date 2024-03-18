import requests
import json
import wordcloud
import matplotlib.pyplot as plt
key = ''
def f1():
    movie = input('请输入你要查询的电影名称：')
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
    plotLocal = list(data['plotLocal'])
    for i in range(len(plotLocal)):
        if (i+1)%80 == 0:
            plotLocal.insert(i,'\n')
    plotLocal = ''.join(plotLocal)
    directors = data['directors']
    actorList = data['actorList'][:3]
    print('电影名:', title)
    print('国家:', countries)
    print('评分:', imDbRating)
    print('评分人数:', imDbRatingVotes)
    print('语言:', languages)
    print('导演:',directors)
    print('主演:',','.join([i['name'] for i in actorList]))
    print('简介:',plotLocal)
    c = input('是否展示词云图？(是/否)')
    if c == '是':
        url = f'https://imdb-api.com/zh/API/Reviews/{key}/{mid}'
        res = requests.get(url)
        data = json.loads(res.text)['items']
        contents = ' '.join([i['content'] for i in data])
        wc = wordcloud.WordCloud()
        wc.generate(contents)
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
    else:
        return 0
def f2():
    movie = input('请输入你要展示的电影名称：')
    url = f'https://imdb-api.com/zh/API/SearchMovie/{key}/{movie}'
    res = requests.get(url)
    data = json.loads(res.text)['results'][0]
    mid = data['id']
    url = f'https://imdb-api.com/zh/API/Reviews/{key}/{mid}'
    res = requests.get(url)
    data = json.loads(res.text)['items']
    contents = ' '.join([i['content'] for i in data])
    wc = wordcloud.WordCloud()
    wc.generate(contents)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
def f3():
    url = f'https://imdb-api.com/zh/API/InTheaters/{key}'
    res = requests.get(url)
    data = json.loads(res.text)['items']
    for i in data:
        print('电影名:', i['title'])
        print('导演:', i['directors'])
        print('主演:', i['stars'])
        print('时长:', i['runtimeStr'])
        print('\n')
info = """

    欢迎来到电影查询系统

1.查询电影具体信息
2.展示电影评论词云
3.查看热映电影
4.退出

"""
while True:
    print(info)
    c = input('请输入你的选择：')
    if c == '1':
        f1()
    elif c == '2':
        f2()
    elif c == '3':
        f3()
    else:
        break