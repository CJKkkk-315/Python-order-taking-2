""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import random
import re
import os
import math

from User import User
from Course import Course
from Review import Review
#
class Admin(User):
    def __init__(self,id: int = -1,username: str="",password: str=""):
        User.__init__(self, id, username, password)

    def register_admin(self):
        f=open('user_admin.txt','r')
        f1= f.readlines()
        if len(f1)==0:
            f_w = open('user_admin.txt', 'a')
            f_w.write(str(self.id) + ";;;" + self.username + ";;;" + self.encryption(self.password) + '\n')
            f_w.close()
        else:

            for i in f1:
                if self.username not in i:
                    f_w=open('user_admin.txt','a')
                    f_w.write(str(self.id)+";;;" + self.username + ";;;"+ self.encryption(self.password)+'\n')
                    f_w.close()

        f.close()
    # pass
    def extract_course_info(self):
        f = open('data/course_data/raw_data.txt', 'r')
        f1 = f.readlines()
        courses = []
        for lines in f1:
            course_id = re.findall(r'"course","id":(.*?),"', lines)
            course_title = re.findall(r'"course","id":.*?,"title":(.*?),', lines)
            image_100x100 = re.findall(r'course":.*?"image_100x100":(.*?),', lines)
            headline = re.findall(r'"headline":(.*?),"num_subscribers"', lines)
            num_of_subscribers = re.findall(r'"num_subscribers":(.*?),', lines)
            avg_rating = re.findall(r'"avg_rating":(.*?),', lines)
            course_content_length = re.findall(r'"content_info":(.*?),', lines)
            course_info = list(zip(course_id, course_title, image_100x100, headline, num_of_subscribers, avg_rating,
                                   course_content_length))
            for x in course_info:
                courses.append(";;;".join(list(x)))

        f_w = open('course.txt', 'w+')
        for lines in courses:
            f_w.write(lines)
            f_w.write('\n')
        f_w.close()
#
#
#
#
#
# extract_course_info()

    def extract_review_info(self):
        f_w = open('review.txt', 'w')
        f_w.close()
        rfile = os.listdir('./data/review_data/')
        for i in rfile:
            path = './data/review_data/' + i
            f = open(path, 'r')
            lines = f.read().replace("null", "None")
            review_dict = eval(lines)
            f_w = open("review.txt", "a")
            for x in range(len(review_dict['results'])):
                review_id = review_dict['results'][x]['id']
                review_content = review_dict['results'][x]['content']
                review_rating = review_dict['results'][x]['rating']
                course_id = i.split(".")[0]
                f_w.write(str(review_id) + ";;;" + review_content + ";;;" + str(review_rating) + ";;;" + str(course_id))

            f.close()
            f_w.close()
    #
    #
    # extract_review_info()




    def extract_students_info(self):
        f_w=open('user_student.txt','w')
        f_w.close()
        rfile=os.listdir('./data/review_data/')
        for i in rfile:
            path ='./data/review_data/'+i
            f=open(path,'r')
            lines = f.read().replace("null", "None")
            review_dict=eval(lines)
            f_w=open('user_student.txt','a')
            for x in range(len(review_dict['results'])):
                review_id = review_dict['results'][x]['id']
                try:
                    id=review_dict['results'][x]['user']['id']
                except KeyError:
                    id=self.generate_unique_user_id()
                else:
                    user_title = review_dict['results'][x]['user']['title']
                    user_image_50x50 = review_dict['results'][x]['user']['image_50x50']
                    user_initials = review_dict['results'][x]['user']['initials']
                    username = user_title.replace(" ", "_").lower()
                    password = user_initials.lower() + str(id) + user_initials.lower()
                    f_w.write(str(id) + ";;;" + username + ";;;" + self.encryption(str(password)) + ";;;" + user_image_50x50 + ";;;" + user_initials + ";;;" + str(review_id))

            f.close()
            f_w.close()


    def extract_instructor_info(self):
        f_w=open('user_instructor.txt','w')
        f_w.close()
        rfile='data/course_data/raw_data.txt'
        for i in rfile:
            path='data/course_data/raw_data.txt'
            f=open(path,'r')
            lines = f.readline().replace("null", "None")
            lines= lines.replace("true",'True')
            lines= lines.replace("false",'False')
            review_dict = eval(lines)
            f_w=open('user_instructor.txt','a')
            for x in range(len(review_dict['results'])):
                id=review_dict['results'][x]['visible_instructor']['id']
                display_name=review_dict['results'][x]['visible_instructor']['display_name']
                job_title=review_dict['results'][x]['visible_instructor']['job_title']
                image_100x100=review_dict['results'][x]['visible_instructor']['image_100x100']
                username=display_name.replace(" ", "_").lower()
                password=id
                course_id=review_dict['results'][x]['course']['id']
                f_w.write(str(id)+";;;"+username+";;;"+self.encryption(password)+";;;"+job_title+";;;"+image_100x100+";;;"+str(course_id))

            f.close()
            f_w.close()






    #
    #
    #
    #
    #
    def extract_info(self):
        print('Start Extraction')
        self.extract_course_info()
        self.extract_students_info()
        self.extract_review_info()
        print('Extraction process finished')
    #
    def remove_data(self):
        choice= input('Press "Y" if you want to erase all data')
        if choice == 'Y':
            f1=open('course.txt','r+')
            f1.truncate(0)
            f1.close()
            f2 = open('review.txt', 'r+')
            f2.truncate(0)
            f2.close()
            f3 = open('user_student.txt', 'r+')
            f3.truncate(0)
            f3.close()
            f4 = open('user_instructor.txt', 'r+')
            f4.truncate(0)
            f4.close()
            print('All data has been eliminated')

    def view_courses(self,args=[]):
          if len(args)==0:
              return Course.course_overview()
          elif len(args)==2:
              if args[0]=='TITLE_KEYWORD':
                  return Course.find_course_by_title_keyword(args[1])
              elif args[0]=='ID':
                  return Course.find_course_by_id(args[1])
              elif args[0]=='INSTRUCTOR_ID':
                  return Course.find_course_by_instructor_id(args[1])

    def view_users(self):
        f=open('user_admin.txt','r')
        lines=f.readlines()
        print(f'total_number_of_admin: {len(lines)}')
        f=open('user_student.txt','r')
        lines=f.readlines()
        print(f'total_number_of_student: {len(lines)}')
        f = open('user_instructor.txt', 'r')
        lines = f.readlines()
        print(f'total_number_of_instructor: {len(lines)}')

    def view_reviews(self,args=[]):
            if len(args) == 0:
                return Review.review_overview()
            elif len(args) == 2:
                if args[0] == 'KEYWORD':
                    return Review.find_review_by_keyword(args[1])
                elif args[0] == 'ID':
                    return Review.find_review_by_id(args[1])
                elif args[0] == 'COURSE_ID':
                    return Review.find_review_by_course_id(args[1])













