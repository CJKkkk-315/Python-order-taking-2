""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import random
import re
import os
import math

class User:
   def __init__(self,id: int = -1, username: str = "", password: str = ""):
      self.id = id
      self.username = username
      self.password = password

   def generate_unique_user_id(self):
      #generate unique id for admin
      user_id_list=[]
      f= open('user_admin.txt','w+')
      lines = f.readlines()
      # generate unique id for instructor
      for i in lines:
         user_id_list.append(i.split(";;;")[0])
      f = open('user_instuctor.txt', 'w+')
      lines = f.readlines()
      #generate unique id for student
      for i in lines:
         user_id_list.append(i.split(";;;")[0])
      f = open('user_student.txt', 'w+')
      lines = f.readlines()
      for i in lines:
         user_id_list.append(i.split(";;;")[0])
      #how unique id is generated (random id)
      random_id=str(random.randint(1000000000, 9999999999))
      for id in user_id_list:
         if random_id==id:
            random_id = str(random.randint(1000000000, 9999999999))
      return random_id
      f.close()



   def encryption (self,input_str):
      all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
      result = ""
      start = "^^^"
      end = "$$$"
      a = 1
      # decide the type and quantity of punctuation to use in encryption
      first = all_punctuation[len(input_str) % len(all_punctuation)]
      second = all_punctuation[len(input_str) % 5]
      third = all_punctuation[len(input_str) % 10]
      result += start
      # insert punctuation into the password and loop
      for index in input_str:
         if a % 3 == 1:
            result += (first + index + first)
         elif a % 3 == 2:
            result += (second * 2 + index + second * 2)
         elif a % 3 == 0:
            result += (third * 3 + index + third * 3)
         a += 1
      result += end
      return result


   def login(self):
      login_result = False
      login_user_role = ''
      login_user_info = ''
      #define user's role and check whether the user is already exist in the user_admin.txt
      f=open('user_admin.txt','r+')
      lines=f.readlines()
      for i in lines:
         if self.username in i.split(";;;")[1] and self.encryption(self.password) in i.split(";;;")[2] :
            login_result=True
            login_user_role='Admin'
            login_user_info=i
      # define user's role and check whether the user is already exist in the user_student.txt
      f = open('user_student.txt', 'r')
      lines = f.readlines()
      for i in lines:
         if i.split(";;;")[1] == self.username and i.split(";;;")[2] == self.encryption(self.password):
            login_result = True
            login_user_role = 'Student'
            login_user_info = i
      # define user's role and check whether the user is already exist in the user_instrutor.txt
      f = open('user_instructor.txt', 'r')
      lines = f.readlines()
      for i in lines:
         if i.split(";;;")[1] in self.username and i.split(";;;")[2] in self.encryption(self.password):
            login_result = True
            login_user_role = 'Instructor'
            login_user_info = i
      f.close()
      return (login_result,login_user_role,login_user_info)

   #show user who do not have permission to extract information
   def extract_info(self):
      print("You have no permission to extract information")

   # show user who do not have permission to view courses
   def view_courses(self,args=[]):
      print("You have no permission to view courses")

   # show user who do not have permission to view users
   def view_users(self):
      print("You have no permission to view users")

   # show user who do not have permission to view reviews
   def view_review(self,arg=[]):
      print("You have no permission to view reviews")

   # show user who do not have permission to remove data
   def remove_data(self):
      print("You have no permission to remove data")

   def __str__(self):
      s = str(self.id) + ";;;" + self.username + ";;;"+ self.password
      return s

