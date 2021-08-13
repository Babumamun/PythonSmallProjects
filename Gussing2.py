from tkinter import *
import random
import time


attempts = 10
last_computer_guess_higher = 100
last_computer_guess_lower = 1


answer = random.randint(1, 100)


def guess_computer(starting_point, ending_point):
    answer_from_computer = random.randint(starting_point, ending_point)
    return answer_from_computer


def setComputerIdea(flag, guesed):
    global last_computer_guess_higher
    global last_computer_guess_lower

    if flag == 1:
        last_computer_guess_lower = guesed+1
    elif flag == -1:
        last_computer_guess_higher = guesed-1


def check_computer_guess(answer, guess):
    global text2

    if answer == guess:
        text2.set("Computer win! Congrats guessed: "+str(guess))
        btn_check.pack_forget()

    elif guess < answer:
        text2.set("Incorrect! computer guessed : "+str(guess)+" too small")
        setComputerIdea(1, guess)

    elif guess > answer:
        text2.set("Incorrect! computer guessed : " + str(guess) + " too big")
        setComputerIdea(-1, guess)


def check_user_answer(answer, guess):
    global attempts
    global text

    attempts -= 1

    if answer == guess:
        text.set("You win! Congrats")
        btn_check.pack_forget()
    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have "+str(attempts)+" attempts - too small")

    elif guess > answer:
        text.set("Incorrect! You have "+str(attempts)+" attempts - too Big")


def check_answer():

    guess = int(entry_window.get())
    check_user_answer(answer, guess)
    c_guess = guess_computer(last_computer_guess_lower,last_computer_guess_higher)
    check_computer_guess(answer, c_guess)
    return


root = Tk()

root.title("Guess The Number")
root.geometry("600x300+50+50")


label = Label(root, text="Guess the Number between 1 & 100",font =("Algerian",16),foreground ='red')
label.pack()

entry_window = Entry(root, width=20, borderwidth=5,font =("Algerian",16),foreground ='blue')
entry_window.pack()


text = StringVar()
text.set("You have 10 attempts! Good luck!")

text2 = StringVar()

text2.set("Computer")

guess_attempts = Label(root, textvariable=text,font =("Algerian",16),foreground ='magenta')
guess_attempts.pack()

msg = Label(root, textvariable=text2,font =("Algerian",16),foreground ='black')
msg.pack()

btn_check = Button(root, text="Check", command=check_answer,font =("Algerian",16),foreground ='green',pady=10)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy,font =("Algerian",16),foreground ='red',pady=10)
btn_quit.pack()


root.mainloop()
