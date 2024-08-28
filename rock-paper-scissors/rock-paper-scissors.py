import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Please enter on the below!")
        continue

    random_number = random.randrange(0,3)
    #rock:0 , paper:1, scissors:2

    computer_pick = options[random_number]
    print("Computer picked",computer_pick+".")

    if user_input == "rock" and computer_pick == "scissors":
        print("User wins!")
        user_wins+=1
    elif user_input == "paper" and computer_pick == "rock":
        print("User wins!")
        user_wins+=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("User wins!")
        user_wins+=1
    elif user_input == computer_pick:
        print("Draw!")
    else:
        print("You lost!")
        computer_wins+=1

print("User won",user_wins,"times.")
print("GoodBye!!")


