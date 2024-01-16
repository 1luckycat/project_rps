# Project Rock, Paper, and Scissors 
# Team members: Liz and Mo



# If player and computer choose the same decision then display ("Game Tied"), 

# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will 
# then end and display ("Thank you for playing").

# import random

# while True:
#     move = ["rock", "paper", "scissors"]
#     player = input("Please select (rock, paper, scissors):")
#     computer = random.choice(move)
    
#     print(f" player picked {player}, computer picked {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("You loose! Better luck next time!")
#     elif player == "scissors":
#         if computer == "rock":
#             print("You loose! Better luck next time")
#     elif player == "paper":
#         if computer == "scissors":
#             print("You loose! Better luck next time!")
#     elif player == "paper":
#         if computer == "rock":
#             print("You Win! Way to go!")
#     elif player == "rock":
#         if computer == "scissors":
#             print("You Win! Way to go!")
#     elif player == "scissors":
#         if computer== "paper":
#             print("You Win!Way to go!")
           
#     rematch = input("Would you like a rematch? (Type: yes or no)")
#     if rematch.lower() == "yes":
#         continue
#     else:
#         print("Good game, thanks for playing")
#         break

