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
    Froz = True
    Qowle = True

    while Froz and Qowle not in options:
        Froz = input("Froz: Mid dooro (rock, paper, scissors): ")
        Qowle = input("Qowle:  Mid dooro  (rock, paper, scissors): ")

    print(f'Froz: {Froz}')
    print(f'Qowle: {Qowle}')

    # if Froz == Qowle:
    #     print("it's a tie")
    # elif Froz == "rock" and Qowle == "scissors":
    #     print("waad guulaysatay")
    # elif Froz == "paper" and Qowle == "rock":
    #     print("waad guulaysatay")
    # elif Froz == "scissors" and Qowle == "paper":
    #     print("waad guulaysatay")
    # else:
    #     print("waad khashirtay")

    if Froz == Qowle:
        print("It's a tie!")
    elif (Froz == "rock" and Qowle == "scissors") or (Froz == "paper" and Qowle == "rock") or (Froz == "scissors" and Qowle == "paper"):
        print("Froz wins!")
    else:
        print("Qowle wins!")

    # if not input("Markale ciyaar? (y/n): ").lower() == "y":
    #     game_on = False
    #     # break

    play_again = input("Markale ciyaar? (y/n): ").lower()
    if play_again == "y":
        game_on = True
    elif play_again == "n":
        game_on = False
    elif not play_again == "y" or "n":
        print(play_again)
        break

print("Mahadsanid!")





















