import random

rock = 1
paper = 2
scissors = 3

user_wins = 0
computer_wins = 0
tie = 0
options = [rock, paper, scissors]
optionsStr = ['', 'rock', 'paper', 'scissors']


print("game rules: \n""rock = 1\npaper = 2\nscissors = 3\n"
      "rock(1) vs scissors(3) --> rock(1) wins\n"
      "scissors(3) vs paper(2) --> scissors(3) wins\n"
      "paper(2) vs rock(1) --> paper(2) wins\n")

while True:
    user_input = int(input("type 1(Rock) 2(Paper) 3(scissors) : "))

    if user_input not in options:
        print("error, please enter the correct number ")
        continue

    random_number = int(random.randint(0, 2))
    # rock : 0, paper : 1, scissors: 2

    computer_pick = (options[random_number])
    print("computer picked", optionsStr[computer_pick], ".")
    if user_input == 1 and computer_pick == 3:
        print("rock(1) wins scissors(3)\n""you won!")
        user_wins += 1

    elif user_input == 3 and computer_pick == 2:
        print("scissors(3) wins paper(2)\n""you won!")
        user_wins += 1

    elif user_input == 2 and computer_pick == 1:
        print("paper(2) wins rock(1)""you won!")
        user_wins += 1

    elif user_input == 3 and computer_pick == 1:
        print("rock(1) wins scissors(3)\n""you lost!")
        computer_wins += 1

    elif user_input == 2 and computer_pick == 3:
        print("scissors(3) wins paper(2)\n""you lost!")
        computer_wins += 1

    elif user_input == 1 and computer_pick == 2:
        print("paper(2) wins rock(1\n)""you lost!")
        computer_wins += 1

    elif user_input == 1 and computer_pick == 1:
        print("rock(1) vs rock(1)\n""tie!")
        tie += 1

    elif user_input == 2 and computer_pick == 2:
        print("paper(2) vs paper(2)\n""tie!")
        tie += 1

    elif user_input == 3 and computer_pick == 3:
        print("scissors(3) vs scissors(3)\n""tie")
        tie += 1

    rematch = input("do you want play again yes(y) or no(n) :").lower()
    yes = "y"
    no = "n"

    while rematch != yes and rematch != no:
        print("error, please enter the correct word ")
        rematch = input("do you want play again yes(y) or no(n) :").lower()

    if rematch == no:
        print("okay bye ):")
        print("computer wins", computer_wins, "times!")
        print("user wins", user_wins, "times!")
        print("tie", tie, "times!")
        print("goodbye!")
        break

    if rematch == yes:
        print("lets play again!")
        continue



