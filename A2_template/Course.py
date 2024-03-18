""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import random
import re
import os
import math

class Course:
    def __init__(self,course_id =-1,course_title: str = "",course_image_100x100: str = "",course_headline: str = "",course_num_subscribers=-1,course_avg_rating: float=-1, course_content_length: float =-1):
        self.course_id=course_id
        self.course_title=course_title
        self.course_image_100x100=course_image_100x100
        self.course_headline=course_headline
        self.course_num_subscribers=course_num_subscribers
        self.course_avg_rating=course_avg_rating
        self.course_content_length=course_content_length

    def find_course_by_title_keyword(self,keyword):
        result_list=[]
        f=open('course.txt','r')
        keyword=eval('r\'.*' +keyword+'.*\'')
        for info in f:
            course_info=info.split(';;;')
            matching=re.match(keyword,info[1])
            if matching:
                result_list.append(Course(int(course_info[0]),course_info[1],course_info[2],course_info[3],int(course_info[4],course_info[5],course_info[6])))
        return result_list


        pass

    def find_course_by_id(self,course_id):
        f=open('course.txt','r')
        for info in f:
            course_info=info.strip().split(';;;')
            if str(course_id)==course_info[0]:
                return course_info
                break
        return None
        f.close()
        pass

    def find_course_by_instructor_id(self,instructor_id):
        course_list=[]
        f=open('user_instructor.txt','r')
        for info in f:
            instructor_info=info.strip().split(';;;')
            if str(instructor_id)==instructor_info[0]:
                return instructor_info[6]
                break
        return(course_list)

    def course_overview (self):
        num_courses=0
        f=open('course.txt','r')
        for info in f:
            num_courses+=1
        f.close()
        return str(num_courses)

    def __str__(self):
        return str([self.course_id,self.course_image_100x100,self.course_headline,self.course_num_subscribers,self.course_avg_rating,self.course_content_length])
    pass









