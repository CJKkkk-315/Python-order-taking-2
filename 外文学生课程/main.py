from basic_class import *
management = CourseManagement()
courses = []
students = []
info = """
#####################################################################
############# Welcome to our course registration system! ############
#####################################################################
#############    1. Course registration for new user   ##############
#############    2. Modify user course registration    ##############
#############    3. Course management                  ##############
#############    4. Print selected course schedule     ##############
#############    5. Query grades and credits           ##############
#############    6. Exit                               ##############
#####################################################################
"""
def load():
    with open('course.txt','r') as f:
        data = f.readlines()
        for i in data:
            t = i.replace('\n','').split(',')
            courses.append(Course(t[0],t[1],t[2],t[3],t[4],t[5]))
    with open('student.txt', 'r') as f:
        data = f.readlines()
        for i in range(0,len(data),2):
            t = data[i].replace('\n', '').split(' ')
            id = t[0]
            s = Student(t[0], t[1], t[2], t[3], t[4], t[5])
            t = data[i+1].replace('\n','').split(' ')
            for j in t:
                s.course.append(j)
            for j in s.course:
                management.add_student(j, id)
            students.append(s)
load()
def f1():
    id = input('Please enter student id:')
    lastname = input('Please enter lastname:')
    firstname = input('Please enter firstname:')
    gender = input('Please enter gender:')
    birthday = input('Please enter birthday:')
    department = input('Please enter department:')
    cs = input('Please enter course id(separated by ,):')
    s = Student(id,lastname,firstname,gender,birthday,department)
    for i in cs.split(','):
        s.add_course(i)
    students.append(s)
    for i in s.course:
        management.add_student(i,id)
    print('Success!')
def f2():
    id = input('Please enter student id:')
    for i in students:
        if i.id == id:
            cs = input('Please enter new course id(separated by ,):')
            i.course = []
            for j in cs.split(','):
                i.add_course(j)
            print('Success!')
            return 0
    print('Error!')
def f3():
    info = """
    1.Set student score
    2.Return all information
    """
    print(info)
    c = input('Please enter your choose:')
    if c == '1':
        sid = input('Please enter student id:')
        cid = input('Please enter course id:')
        score = input('Please enter score:')
        management.set_score(cid,sid,score)
    elif c == '2':
        cid = input('Please enter course id:')
        data = management.returns(cid)
        l = []
        for d in data:
            for i in students:
                if d[0] == i.id:
                    print('name:',i.lastname,i.firstname,'score:',d[1])
                    l.append(int(d[1]))
        print('max score',max(l))
        print('average score',sum(l)/len(l))
def f4():
    sid = input('Please enter student id:')
    for i in students:
        if i.id == sid:
            s = i
    for i in courses:
        if i.id in s.course:
            print('name:',i.name)
            print('time:',i.time)
            print('localtion:',i.location)
def f5():
    sid = input('Please enter student id:')
    cid = input('Please enter course id:')
    for i in management.returns(cid):
        if i[0] == sid:
            print('score:',i[1])
    for i in courses:
        if i.id == cid:
            print('credits:',i.credits)
def f6():
    with open('student.txt','w') as f:
        for i in students:
            f.write(' '.join([i.id,i.lastname,i.firstname,i.gender,i.birthday,i.department])+'\n')
            f.write(' '.join(i.course)+'\n')
while True:
    print(info)
    c = input('Please enter your choose:')
    if c == '1':
        f1()
    elif c == '2':
        f2()
    elif c == '3':
        f3()
    elif c == '4':
        f4()
    elif c == '5':
        f5()
    elif c == '6':
        f6()
        break