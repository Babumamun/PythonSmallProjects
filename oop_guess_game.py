import random
class GuessGame:
    print("*****Welcome to guessGame*****")
    '''minum = 1
    maxnum = 100'''

    def generates_guess_number(self):
        secret_number = random.randint(1, 100)  # this is answer
        return secret_number

    def enter_your_number(self):
        your_guess = int(input("Please enter an integer："))
        return your_guess

    def main(self,minum, maxnum):
        secret_number = self.generates_guess_number()
        # print(secret_number)
        while True:
            # you are guessing a number
            your_guess = self.enter_your_number()
            if your_guess == secret_number:
                print("Congradulations，you win！")
                self.try_again()
                break

            elif your_guess > secret_number and your_guess < self.maxnum:
                self.maxnum = your_guess  # get  new maxnum value
                print("Your guess is too high！")
            elif your_guess < secret_number and your_guess > minum:
                minum = your_guess  # get  new minum value
                print("Your guess is too low！")

            # computer generates a number
            self.Computer_guess_nuber(minum, maxnum)

    def Computer_guess_nuber(self,minum, maxnum):
        secret_number = self.generates_guess_number()
        while True:
            com_guess = random.randint(minum, maxnum)  # use new  new minum value and new maxnum value
            print("the computer enter a number:" + str(com_guess))
            if com_guess == secret_number:
                print("Smart,computer win！")
                self.try_again()
                break
            elif com_guess > secret_number:
                self.maxnum = com_guess
                print("The Computer guess is too high！")
                break
            elif com_guess < secret_number:
                self.minum = com_guess
                print("The Computer guess is too low！")
                break

    def try_again(self):
        keep_playing = input("Do u wanna play again?yes or no:\n")
        if keep_playing.lower() == "yes":
            self.main(1, 100)
        else:
            exit()



obj=GuessGame()
obj.main(1,100)
