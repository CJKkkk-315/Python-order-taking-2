""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
from User import *
class Student(User):
    def __init__(self,id=-1,username: str="",password: str="",user_title: str="",user_image_50x50:str="",user_initials:str="",review_id=-1):
        User.__init__(self, id, username, password)
        self.user_title=user_title
        self.user_image_50x50=user_image_50x50
        self.user_initials=user_initials
        self.review_id=review_id

    def view_courses(self,args=[]):

        pass
    def view_review(self,arg=[]):
        pass
    def __str__(self):
        return(self.id,self.username,self.password,self.user_title,self.user_image_50x50,self.user_initials,self.review_id)
    pass


