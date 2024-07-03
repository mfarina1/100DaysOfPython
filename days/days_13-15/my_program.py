from my_actors import Creech, Sorceror, Reptile
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('---------------------------------')
    print('          D&D GAME')
    print('---------------------------------')
    print()

def game_loop():
    creatures = [
        Creech('Spider', 1),
        Creech('Bat', 3),
        Creech('Blob', 5),
        Reptile('Alligator', rating=25, color="green", is_magical=False),
        Reptile('Wyvern', rating=50, color="orange", is_magical=True),
        Sorceror('Fire sorceror', 100)
    ]

    main_character = Sorceror('Madeline', 88)

    while True:

        current_creech = random.choice(creatures)
        print('A {}, rating {}, has appeared from the scary forest...'
              .format(current_creech.name, current_creech.rating))
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [p]erception check? ')

        if cmd == 'a':
            if main_character.attack(current_creech):
                creatures.remove(current_creech)
                print("The sorceror defeated {}".format(current_creech.name))
            else:
                print("The sorceror has been defeated by the powerful {}".format(current_creech.name))
        elif cmd == 'r':
            print("The sorceror is a coward!")
        elif cmd == 'p':
            print('The sorceror {} takes in her surroundings and sees: '.format(main_character.name))
            for i in creatures:
                print(" * {} of rating {}".format(
                    i.name, i.rating
                ))
        else:
            print("Exiting game, goodbye!")
            break

        if not creatures:
            print("You've won!")
            break

        print()


if __name__ == '__main__':
    main()