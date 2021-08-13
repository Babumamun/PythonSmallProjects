student_final_grade = []
class Input:
    def __init__(self,roll_num,scr_chinese,scr_python,scr_of_SE):
        self.roll_num=roll_num
        self.scr_chinese=scr_chinese
        self.scr_python=scr_python
        self.scr_of_SE=scr_of_SE


def chose_option():
    print("................***************....................")
    print("------- Welcome to Student final grade System ------")
    print("********.....................................*******")
    print('A: Add student final grade' )
    print('L: List all students')
    print('C: Take score of Chinese for sort')
    print('T: Take total score for sort')
    print('Q: Quit')


def interact_with_option():
    chose_option()
    while True:
        try:
            user_input = input("Enter a choice:A/L/C/T/Q:")
            if user_input.isdigit():
                raise Exception
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
    chec_duplicate = [student for student in student_final_grade if student[0]== roll_num]
    if chec_duplicate == []:
        new_student = [roll_num, scr_chinese, scr_python,scr_of_SE]
        student_final_grade.append(new_student)
        print("Student successfully added!")
    else:
        print("This RollNumber is not available!")
        tryAgain()

def student_list():
    print(student_final_grade)
    tryAgain()

def short_by_chinese():
    print("Original List is:",student_final_grade)
    #student_final_grade.sort(key=lambda x:(x[1],x[1]))
    student_final_grade.sort(key=lambda x: (x[1]))
    print("After short by chinese the list is:",student_final_grade)
    tryAgain()
#aList = [["Jone",68,72],["Lily",75,89],["Bill",83,70],["Annie",73,78]]
#aList.sort(key=lambda x:x[2])
def short_by_total():
    print("Original List is:",student_final_grade)
    student_final_grade.sort(key=lambda x:x[1]+x[2]+x[3])
    #student_final_grade.sort(key=lambda x: (x[4]))

    print("After short by total the list is:", student_final_grade)
    tryAgain()




def tryAgain():
        try:
            user_input = input("Do You want to Try again?Yes/No\n")
            if user_input.isdigit():
                raise Exception
            elif user_input.upper() == "YES":
                interact_with_option()
            elif user_input.upper() == "NO":
                quit()
        except ValueError as e:
            print("invalid Input !Please input letter!")

interact_with_option()
