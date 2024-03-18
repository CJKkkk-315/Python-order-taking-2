""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import random
import re
import os
import math

class Review:
    def __init__(self,id=-1,content: str="",rating: float=-1.0,course_id=-1):
        self.id=id
        self.content=content
        self.rating=rating
        self.course_id=course_id

    def find_review_by_id(self,review_id):
        f=open('review.txt','r')
        for info in f:
            review_info=info.split(';;;')
            if review_id==review_info[0]:
                return
                break
            return None

    def find_review_by_keyword(self,keyword):
        result_list=[]
        f=open('review.txt','r')
        keyword=eval('r\'.*' +keyword+'.*\'')
        for info in f:
            review_info=info.split(';;;')
            matching=re.match(keyword,review_info[1])
            if matching:
                result_list.append()

    def find_review_by_course_id(self,course_id):
        course_list = []
        f = open('review.txt', 'r')
        for info in f:


            pass

    def review_overview(self):
        num_courses = 0
        f = open('review.txt', 'r')
        for info in f:
            num_courses += 1
        f.close()
        return str(num_courses)
        pass

    def __str__(self):
        return (self.id,self.content,self.rating,self.course_id)


