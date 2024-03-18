data = []
def load():
    global data
    with open('student.txt','r') as f:
        data = f.readlines()
        data = [i.replace('\n','').split() for i in data]
def add():
    s = input('请输入学号，姓名，是否缺勤和考试成绩（以空格分隔）：\n').split()
    data.append(s)
    with open('student.txt', 'a+') as f:
        f.write(' '.join(s) + '\n')
def check():
    for i in range(len(data)):
        print(data[i][1],'是否缺勤？(是/否)')
        c = input()
        data[i][2] = c
    with open('student.txt', 'w') as f:
        for s in data:
            f.write(' '.join(s) + '\n')
def show():
    print('已到学生：')
    for i in data:
        if i[2] == '否':
            print(i[1],end=' ')
    print('\n',end='')
    print('未到学生：')
    for i in data:
        if i[2] != '否':
            print(i[1], end=' ')
def back():
    name = input('请输入后报道学生姓名:')
    for i in range(len(data)):
        if data[i][1] == name:
            data[i][2] = '否'
            print('补签到成功')
            with open('student.txt', 'w') as f:
                for s in data:
                    f.write(' '.join(s) + '\n')
            return
    print('不存在该学生。')
def change():
    name = input('请输入要修改的学生姓名:')
    for i in range(len(data)):
        if data[i][1] == name:
            qd = input('请输入该学生是否缺勤:')
            score = input('请输入该学生考试成绩:')
            data[i][2] = qd
            data[i][3] = score
            print('修改成功成功')
            with open('student.txt', 'w') as f:
                for s in data:
                    f.write(' '.join(s) + '\n')
            return
    print('不存在该学生。')
def main():
    while True:
        menu = """
        1.添加学生
        2.开始点名
        3.统计
        4.添加后报道学生
        5.修改学生信息
        6.退出
        """
        print(menu)
        choose = input('输入选项：')
        if choose == '1':
            add()
        elif choose == '2':
            check()
        elif choose == '3':
            show()
        elif choose == '4':
            back()
        elif choose == '5':
            change()
        elif choose == '6':
            break
        else:
            print('输入错误')
load()
main()