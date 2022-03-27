import tkinter as TK
import tkinter.simpledialog as SD
import tkinter.messagebox as MB
import random as RD
def rockpaperscissors():
    computerpoints = 0
    userpoints = 0
    while True:
        while True: 
            user = SD.askstring("ROCK PAPER SCISSORS", "Type R for Rock, P for Paper, or S for Scissors")
            user = user.upper()
            if user == 'R' or 'P' or 'S':
                break
            else:
                MB.showerror("ERROR", "TRY AGAIN")
        
        computer = RD.randint(1,3)
        if computer == 1:
            computer = "R"
        if computer == 2:
            computer = "P"
        if computer == 3:
            computer = "S"
        
        if computer == 'R' and user == 'S':
            computerpoints += 1
            MB.showinfo("COMPUTER WINS!", "The computer chose rock and you chose scissors \n\n THE COMPUTER WINS THIS ROUND")
        elif computer == 'P' and user == 'R':
            computerpoints += 1
            MB.showinfo("COMPUTER WINS!", "The computer chose paper and you chose rock \n\n THE COMPUTER WINS THIS ROUND")
        elif computer == 'S' and user == 'P':
            computerpoints += 1
            MB.showinfo("COMPUTER WINS!", "The computer chose scissors and you chose paper \n\n THE COMPUTER WINS THIS ROUND")



        elif user == 'R' and computer == 'S':
            userpoints += 1
            MB.showinfo("YOU WIN!", "The computer chose scissors and you chose rock \n\n YOU WIN THIS ROUND")
        elif user == 'P' and computer == 'R':
            userpoints += 1
            MB.showinfo("YOU WIN!", "The computer chose rock and you chose paper \n\n YOU WIN THIS ROUND")
        elif user == 'S' and computer == 'P':
            userpoints += 1
            MB.showinfo("YOU WIN!", "The computer chose paper and you chose scissors \n\n YOU WIN THIS ROUND")



        elif user == computer:
            MB.showinfo("TIE", "ITS A TIE!")


        if computerpoints == 3:
            MB.showinfo("THE COMPUTER WINS", "YOU LOSE \n\n better luck next time")
            break
        elif userpoints == 3:
            MB.showinfo("CONGRATS!", "YAY, YOU WON!")
            break

rockpaperscissors() 