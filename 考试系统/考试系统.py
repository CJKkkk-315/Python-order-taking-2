import random
questions = []
qid = 1
def load():
    global questions,qid
    with open('file08.txt','r') as f:
        data = f.readlines()
    for i in range(len(data)):
        questions.append(data[i].replace('\n','').split())
        qid += 1
def insert():
    global questions,qid
    s = input('请输入题目，四个选项以及答案（以空格分隔）：\n').split()
    s.insert(0,str(qid))
    questions.append(s)
    with open('file08.txt', 'a+') as f:
        f.write(' '.join(s)+'\n')
def begin():
    test = random.sample(questions,5)
    score = 0
    for i in test:
        for j in i[1:-1]:
            print(j)
        choose = input('请输入您的选项：')
        if choose == i[-1]:
            score += 20
    print('您最终得分：',score)
def main():
    while True:
        menu = """
        1.试题追加
        2.试题抽取
        3.退出系统
        """
        print(menu)
        choose = input('输入选项：')
        if choose == '1':
            insert()
        elif choose == '2':
            begin()
        elif choose == '3':
            break
        else:
            print('输入错误')
load()
main()