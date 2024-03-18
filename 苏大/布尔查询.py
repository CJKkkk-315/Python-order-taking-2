import os
ext = 'txt'
files = os.listdir(os.getcwd()+'/数据文件')
files = [i for i in files if i.split('.')[-1] == ext]
files.sort()
file_decode = {}
file_word_list = {}
for i in range(len(files)):
    file_decode[i] = files[i]
with open('res/index.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for i in lines:
    line = i.replace('\n','').split(' ')
    file_word_list[line[0]] = list(map(int,line[2:]))
while True:
    query = input('输入查询命令：')
    if query == '###':
        break
    query_list = query.split(' ')
    try:
        if len(query_list) == 1:
            l1 = file_word_list[query_list[0]]
            res = [i for i in l1]
            res = list(map(lambda x: file_decode[x], res))
            res.sort()
            for i in res:
                with open('数据文件/' + i, 'r', encoding='utf-8') as f:
                    t = []
                    sentences = f.readlines()
                    for sentence in sentences:
                        if query_list[0] in sentence:
                            t.append(sentence.replace('\n', ''))
                    if t:
                        print(i, end='--')
                        for s in t:
                            print(s, end=';')
                    print('\n')
        elif query_list[1] == 'and':
            l1 = file_word_list[query_list[0]]
            l2 = file_word_list[query_list[2]]
            res = [i for i in l1 if i in l2]
            res = list(map(lambda x:file_decode[x],res))
            res.sort()
            for i in res:
                with open('数据文件/' + i,'r',encoding='utf-8') as f:
                    t = []
                    sentences = f.readlines()
                    for sentence in sentences:
                        if query_list[0] in sentence or query_list[2] in sentence:
                            t.append(sentence.replace('\n',''))
                    if t:
                        print(i,end='--')
                        for s in t:
                            print(s,end=';')
                    print('\n')
        elif query_list[1] == 'or':
            l1 = file_word_list[query_list[0]]
            l2 = file_word_list[query_list[2]]
            res = [i for i in l1 if i not in l2] + l2
            res = list(map(lambda x:file_decode[x],res))
            res.sort()
            for i in res:
                with open('数据文件/' + i,'r',encoding='utf-8') as f:
                    t = []
                    sentences = f.readlines()
                    for sentence in sentences:
                        if query_list[0] in sentence or query_list[2] in sentence:
                            t.append(sentence.replace('\n',''))
                    if t:
                        print(i,end='--')
                        for s in t:
                            print(s,end=';')
                    print('\n')
    except:
        print('不存在这个词语哦')
