import random
secret_number=random.randint(1,100)#this is answer
print("*****Welcome to guessGame*****")
#print(secret_number)
minum = 1
maxnum = 100
while True:
    # you are guessing a number
    your_guess = int(input("Please enter an integer："))
    if your_guess==secret_number:
        print("Congradulations，you win！")
        break
    elif your_guess>secret_number and your_guess < maxnum:
        maxnum = your_guess #get  new maxnum value
        print("Your guess is too high！")
    elif your_guess<secret_number and your_guess > minum:
        minum = your_guess#get  new minum value
        print("Your guess is too low！")

    #computer generates a number
    com_guess=random.randint( minum,maxnum ) #use new  new minum value and new maxnum
    print("the computer enter a number:" + str(com_guess))
    if com_guess == secret_number:
        print("Smart,computer win！")
        break
    elif com_guess > secret_number:
        maxnum = com_guess
        print("The Computer guess is too high！")
    elif com_guess<secret_number:
        minum = com_guess
        print("The Computer guess is too low！")




