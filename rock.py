import random


class Rock:

    def __init__(self,player,computer,rock):
        self.player = player
        self.computer = computer
        self.rock = rock



    def player1(self):
        play = input("Rock,Paper, or Scissors? ")
        self.player = play.lower()
        return self.player

    def comput(self):
        computer_play =  random.choice(["Rock", "Paper", "Scissors"])
        self.computer = computer_play.lower()
        print(f"Computer plays {self.computer}")
    
    def who_wins(self):
        if self.computer == 'rock' and self.player == "paper":
            print("You win!")
        elif self.computer == "paper" and self.player == "rock" :
            print("You lose!")
        elif self.computer == "rock" and self.player == "rock" :
            print("Game Tied!")  
        elif self.computer == "paper" and self.player == "scissors" :
             print("You win!")
        elif self.computer == "scissors" and self.player == "paper" :
            print("You lose!") 
        elif self.computer == "scissors" and self.player == "rock" :
             print("You win!")
        elif self.computer == "rock" and self.player == "scissors" :
            print("You lose!")
        elif self.computer == "paper" and self.player == "paper" :
            print("You lose!")
        elif self.computer == "scissors" and self.player == "scissors" :
            print("Game Tied!") 
        
game = Rock(0,0,0)
def run():
    while True:
        msg = input("Would you like to play? if you would like to quit type 'quit' ")
        if msg.lower() == "yes":
            game.player1()
            game.comput()
            game.who_wins()
        elif msg == "quit":
            break

run()


