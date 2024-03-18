""""
student name: Su Pin Chuan
student id: 31741235
start date: 25/04/2022
"""
import os.path

from User import User
from Admin import Admin
from Student import Student
from Instructor import Instructor
from Course import Course
from Review import Review
def show_menu():

    print("1.EXTRACT_DATA")
    print("2.VIEW_COURSE")
    print("3.VIEW_USER")
    print("4.VIEW_REVIEW")
    print("5.REMOVE_DATA")

def process_operations(user_object):
    option = input()
    while option != "logout":
       if option.split()[0]=='1':
           user_object.extract_info()
       elif option.split()[0]=='2':
           if len(option)==3 and type(user_object).__name__=="Admin":
               args=[option.split()[1],option.split()[2]]
               user_object.view_courses(args)
           else:
               user_object.view_courses(args)
       elif option.split()[0]=='3':
           user_object.view_users()

       elif option.split()[0]=='4':
           if len(option) == 3 and type(user_object).__name__ == "Admin":
               args = [option.split()[1], option.split()[2]]
               user_object.view_reviews(args)
           else:
               user_object.view_reviews(args)

       elif option.split()[0]=='5':
           user_object.remove_data()
       else:
           print ("invalid option")
       print(f'{type(user_object).__name__} login successfully')
       print(f'Welcome{user_object.username}. Your role is {type(user_object).__name__}')
       print(f'Please enter {type(user_object).__name__} command for further service:')
       show_menu()

def main():
    #allow the user to input their username and password
    user_input = input('Please input username and passeword to login:(format username password)\n')
    #as long as the user not input the string "exit" the program will keep looping
    while not user_input=="exit":
        #define the first input of the user as username
        username=user_input.split()[0]
        #define the second input of the user as password
        password=user_input.split()[1]
        #combine the input of the user and call the fuction (login) created in User
        result = User('',username,password).login()
        #define the role of the user
        if result[0] is True:
            #if the user is admin then tell the user which there role is admin
            if result[1] == "Admin":
                user_object=Admin(result[2].split(";;;")[0],result[2].split(";;;")[1],result[2].split(";;;")[2])
                print(f'{result[1]} login successfully')
                print(f'Welcome{username}. Your role is {result[1]}')
                print(f'Please enter {result[1]} command for further service:')
                show_menu()
                process_operations(user_object)
            if result[1] == "Student":
                user_object = Student(result[2].split(";;;")[0], result[2].split(";;;")[1], result[2].split(";;;")[2],result[2].split(";;;")[3], result[2].split(";;;")[4], result[2].split(";;;")[5], result[2].split(";;;")[6])
                print(f'{result[1]} login successfully')
                print(f'Welcome{username}. Your role is {result[1]}')
                print(f'Please enter {result[1]} command for further service:')
                show_menu()
                process_operations(user_object)
            if result[1] == "Instructor":
                user_object = Instructor(result[2].split(";;;")[0], result[2].split(";;;")[1], result[2].split(";;;")[2],result[2].split(";;;")[3], result[2].split(";;;")[4], result[2].split(";;;")[5], result[2].split(";;;")[6])
                print(f'{result[1]} login successfully')
                print(f'Welcome{username}. Your role is {result[1]}')
                print(f'Please enter {result[1]} command for further service:')
                show_menu()
                process_operations(user_object)

        else:
            print('username or password incorrect')
        user_input = input('Please input username and passeword to login:(format username password)\n')

if __name__ == "__main__":
    if not os.path.exists('user_admin.txt'):
        f=open('user_admin.txt','w')
        f.close()
    if not os.path.exists('user_student.txt'):
        f=open('user_student.txt','w')
        f.close()
    if not os.path.exists('user_instructor.txt'):
        f=open('user_instructor.txt','w')
        f.close()
    # print a welcome message
    print("Welcome to our system")
    # manually register admin
    Admin(111111,"admin","admin").register_admin()
    main()







