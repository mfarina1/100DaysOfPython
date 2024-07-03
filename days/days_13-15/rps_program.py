from rps import Roll, Player
import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print()
    player1 = Player(input("Enter your name: "))
    player2 = Player("CPU")
    print()


    game_loop(player1, player2)


def game_loop(player1, player2):

    while True:
        print("rock, paper, or scissors?")
        player1_roll = Roll(input())
        print()

        player2_roll = Roll("")
        rand_idx = random.randint(0, 3)
        if rand_idx == 1:
            player2_roll == "Rock"
        
        if rand_idx == 2:
            player2_roll == "Scissors"

        if rand_idx == 3:
            player2_roll == "Paper"

        print("CPU rolls: ", player2_roll)

        player1_roll.evaluate_roll(player2_roll)

        print()
    

if __name__ == '__main__':
    main()

