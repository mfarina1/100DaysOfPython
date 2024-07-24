import random
import sys
import logbook
import requests.exceptions

possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)

level = logbook.TRACE
log_file = "rps_log.log"

if not log_file:
    logbook.StreamHandler(sys.stdout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_file, level=level).push_application()

app_log = logbook.Logger('App')

class Game_Rock_Paper_Scissors:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer


    def Game(self):
        if self.player == self.computer:
            print("Tie!")
        elif self.player == "rock":
            if self.computer == "paper":
                return "You lose! {1} covers {0}" .format(self.computer,self.player)
            else:
                return "You win! {0} smashes {1}" .format(self.player ,self.computer)
        elif self.player == "paper":
            if self.computer == "scissors":
                return "You lose! {1} cut {0}" .format(self.computer,self.player)
            else:
                return "You win! {0} covers {1}" .format(self.player ,self.computer)
        elif self.player == "scissors":
            if self.computer == "rock":
                return "You lose! {1} smashes {0}" .format(self.computer,self.player)
            else:
                return "You win! {1} cut {0}" .format(self.player ,self.computer)
        

if __name__ == '__main__':
        
    while True:

        try:
            player = input("Enter a choice (rock, paper, scissors): ")
            if player!="rock" and player!="paper" and player!="scissors":
                raise ValueError("That's not a valid play. Check your spelling!")

            print(f"\nYou chose {player}, computer chose {computer}.\n")
            playing = Game_Rock_Paper_Scissors(player, computer)
            print(playing.Game())

        except ValueError:
            msg = "That's not a valid entry. Check your spelling!"
            print("ERROR: " + msg)
            app_log.warn(msg)

        except KeyboardInterrupt:
            msg = "Ending program"
            print("WARNING: " + msg)
            app_log.warn(msg)
            break