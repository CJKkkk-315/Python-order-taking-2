""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import random
import re
import os
import math

from Course import*
from Review import*
from User import*

class Instructor(User):
    def __init__(self,id=-1,username: str="",password: str="",display:str="",job_title:str="",image_100x100:str="",course_id_list:list=[]):
        User.__init__(self,id,username,password)
        self.display=display
        self.job_title=job_title
        self.image_100x100=image_100x100
        self.course_id_list=course_id_list

    def view_courses(self,args=[]):
        course_list= Course.find_course_by_instructor_id(self.id)
        if len(course_list)>10:
            course_list=course_list[0:10]
            print(course_list)
        else:
            print(course_list)

    def view_review(self,arg=[]):

        pass
    def __str__(self):
        return(self.id,self.username,self.password,self.display,self.job_title,self.image_100x100,self.course_id_list)

    pass

