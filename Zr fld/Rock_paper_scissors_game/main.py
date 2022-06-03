import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("pick an option rock, paper, or scissors?: ")

    #validate for capitalised letters with .lower()
    player = player.lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!!!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("Sorry you Lose!!!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("Sorry you Lose!!!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!!!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("Sorry you Lose!!!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!!!")

    play_again = input("Will you like to play again? (yes/no):")
    play_again = play_again.lower()

    if play_again != "yes":
        break

print("Thanks for playing, Hate to see you leave")