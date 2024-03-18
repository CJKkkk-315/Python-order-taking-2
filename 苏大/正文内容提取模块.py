from bs4 import BeautifulSoup
import os
from collections import Counter
import jieba


ext = 'html'
files = os.listdir(os.getcwd()+'\HTMLS')
files = [i for i in files if i.split('.')[-1] == ext]
for i in files:
    with open('HTMLS\\'+i,'r',encoding='utf-8') as f:
        soup = BeautifulSoup(f.read())
        title = soup.find(name='title').text
    with open('数据文件\\' + title + '.txt', 'w', encoding='utf-8') as f:
        content = soup.find(name='body').text.split('\n')
        content = '\n'.join([i for i in content if i])
        content = content.replace('。','。\n')
        f.write(content)


