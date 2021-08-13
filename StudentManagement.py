#student_final_grade = [[10,68,72,89,229],[12,78,73,89,240],[11,69,72,89,230]]
student_final_grade = []#store data in empty list
#[10,68,72,89],[12,78,73,89],[11,69,72,89]
def chose_option():#chose any option
    print("................***************....................")
    print("------- Welcome to Student final grade System ------")
    print("********.....................................*******")
    print('A: Add student final grade' )
    print('L: List all students')
    print('C: Take score of Chinese for sort')
    print('T: Take total score for sort')
    print('Q: Quit')


def interact_with_option():
    chose_option()#called that function 
    while True:
        try:
            user_input = input("Enter a choice:A/L/C/T/Q:")
            if user_input.isdigit():#check user input digit or string 
                raise Exception#catch exception 
            elif user_input.upper()=="A":
              add_student_grade()
            elif user_input.upper()=="L":
               student_list()
            elif user_input.upper()=="C":
                short_by_chinese()
            elif user_input.upper() == "T":
                short_by_total()
            elif user_input.upper() == "Q":
                quit()
        except Exception as e:
            print("invalid Input !Please input a capital letter!")

def add_student_grade():
    while True:
        try:
            roll_num = int(input("Enter a roll number of the student:"))
            scr_chinese =int(input("Enter score of Chinese:"))
            scr_python = int(input("Enter score of Python:"))
            scr_of_SE=int(input("Enter score of SE:"))
        except ValueError as g:
            print("invalid Input !Please input digit!")
        else:
            break
    #check duplicate or not by list comprehensions   
    chec_duplicate = [student for student in student_final_grade if student[0]== roll_num]
    #sum=scr_chinese+scr_python+scr_of_SE
    if chec_duplicate == []:
        #new_student = [roll_num, scr_chinese, scr_python,scr_of_SE,sum]
        new_student = [roll_num, scr_chinese, scr_python,scr_of_SE]
        student_final_grade.append(new_student)#store all value in the list
        print("Student successfully added!")
    else:
        print("This RollNumber is not available!")
        tryAgain()

def student_list():#show all the student in the list 
    print(student_final_grade)
    tryAgain()

def short_by_chinese():#sort by chinese number
    print("Original List is:",student_final_grade)
    #student_final_grade.sort(key=lambda x:(x[1],x[1]))
    student_final_grade.sort(key=lambda x:x[1])#use lambda to sort by index[1]
    print("After short by chinese the list is:",student_final_grade)
    tryAgain()
def short_by_total():#sort by total 
    print("Original List is:",student_final_grade)
    student_final_grade.sort(key=lambda x:x[1]+x[2]+x[3])#sum all socre and sort them
    #student_final_grade.sort(key=lambda x:x[4])
    print("After short by total the list is:", student_final_grade)
    tryAgain()#call function to give another try 




def tryAgain():
        try:
            user_input = input("Do You want to Try again?Yes/No\n")
            if user_input.isdigit():#check user input digit or string 
                raise Exception#catch exception 
            elif user_input.upper() == "YES":
                interact_with_option()
            elif user_input.upper() == "NO":
                quit()
        except ValueError as e:
            print("invalid Input !Please input letter!")

interact_with_option()#call function
