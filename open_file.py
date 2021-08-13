'''op_File=open("text.txt","a")
user_name=input("Please Chose a user name:")
password=input("Please Chose password:")
op_File.write(user_name+" "+password+"\n")
print('Input Success!')
op_File1=open("text.txt","r")
data=op_File1.readlines()
user_dict={}
for i in data:
    user_name,password=i.split()
    user_dict[user_name]=password
print("Do u wanna login?")
op_File.close()
'''
def homepage():
    print(":::::::::::::::::::::::::::::::::::::::::::")
    print(":::::::::::Welcome to Python Class::::::::")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1:Login")
    print("2:Registration")
    print("0:Exit")

def main():
    while True:
        homepage()
        user_chose=int(input("Please input a number:"))
        if user_chose==1:
            login()
        elif user_chose==2:
            registration()
        elif user_chose==0:
            break


def login():
    op_File1 = open("text.txt", "r")
    data = op_File1.readlines()
    user_dict = {}
    for i in data:
        user_name1, password1 = i.split()
        user_dict[user_name1] = password1
    print(user_dict)
    user_name = input("Please Input Your UserName:")
    user_pass = input("Please Input Your Password:")
    if (user_name,user_pass) in user_dict.items():
        print("welcome")
    else:
        print("login failed")


def registration():
    op_File = open("text.txt", "a")
    user_name = input("Please Chose a user name:")
    password = input("Please Chose password:")
    op_File.write(user_name + " " + password + "\n")
    print('Input Success!')



main()
'''if user_name in user_dict:
           print("log in Success!")
           print(user_name+"welcome to Python Class!")
       else:
           print("Invalid user or password!")'''
