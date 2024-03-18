class Course:
    def __init__(self,id,name,department,credits,time,location):
        self.id = id
        self.name = name
        self.department = department
        self.credits = credits
        self.time = time
        self.location = location
class CourseManagement:
    def __init__(self):
        self.data = {}
    def add_student(self,cid,sid):
        try:
            self.data[cid].append([sid,0])
        except:
            self.data[cid] = [[sid,0]]
    def set_score(self,cid,sid,score):
        if cid not in self.data:
            return -1
        for i in self.data[cid]:
            if i[0] == sid:
                i[1] = score
    def returns(self,cid):
        return self.data[cid]
class Person:
    def __init__(self,lastname,firstname,gender,birthday):
        self.lastname = lastname
        self.firstname = firstname
        self.gender = gender
        self.birthday = birthday
class Student(Person):
    def __init__(self,id,lastname,firstname,gender,birthday,department):
        Person.__init__(self,lastname,firstname,gender,birthday)
        self.id = id
        self.department = department
        self.course = []
    def add_course(self,cid):
        self.course.append(cid)
    def dele_course(self,cid):
        try:
            self.course.remove(cid)
        except:
            return -1
    def get_course(self):
        return self.course
