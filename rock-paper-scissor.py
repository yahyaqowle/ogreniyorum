# import random
#
# options = ('rock', 'paper', 'scissors')
#
# game_on = True
#
# while game_on:
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Mid dooro (rock, paper, scissors): ")
#
#     print(f'Player: {player}')
#     print(f'Computer: {computer}')
#
#     if player == computer:
#         print("it's a tie")
#     elif player == "rock" and computer == "scissors":
#         print("waad guulaysatay")
#     elif player == "paper" and computer == "rock":
#         print("waad guulaysatay")
#     elif player == "scissors" and computer == "paper":
#         print("waad guulaysatay")
#     else:
#         print("waad khashirtay")
#
#     if not input("Markale ciyaar? (y/n): ").lower() == "y":
#         game_on = False
#         # break
#
# print("Mahadsanid!")


import random

options = ('rock', 'paper', 'scissors')

game_on = True

while game_on:
    player = True
    computer = True

    while player and computer not in options:
        player = input("Mid dooro PLAYer (rock, paper, scissors): ")
        computer = input("Mid dooro Comp (rock, paper, scissors): ")

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    # if player == computer:
    #     print("it's a tie")
    # elif player == "rock" and computer == "scissors":
    #     print("waad guulaysatay")
    # elif player == "paper" and computer == "rock":
    #     print("waad guulaysatay")
    # elif player == "scissors" and computer == "paper":
    #     print("waad guulaysatay")
    # else:
    #     print("waad khashirtay")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("Player wins!")
    else:
        print("Computer wins!")

    if not input("Markale ciyaar? (y/n): ").lower() == "y":
        game_on = False
        # break

print("Mahadsanid!")





















