# Project Rock, Paper, and Scissors 
# Team members: Liz and Mo



# If player and computer choose the same decision then display ("Game Tied"), 

# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and 
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") 
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will 
# then end and display ("Thank you for playing").


import random


rand = ["rock", "paper", "scissors"]


def the_game():
    print("Welcome! Let's play Rock-Paper-Scissors!")

    p_count = 0
    comp_count = 0
    tie_count = 0

    while True: 
        choice = input("Choose either Rock, Paper, Scissors, or I quit:   ")
        comp_choice = random.choice(rand)
        print("==========================================================================")

        # Tie results
        if choice.lower().strip() == "rock" and comp_choice == "rock":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nGame Tied!\n")
            tie_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            

        elif choice.lower().strip() == "paper" and comp_choice == "paper":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nGame Tied!\n")
            tie_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            

        elif choice.lower().strip() == "scissors" and comp_choice == "scissors":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nGame Tied!\n")
            tie_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            


        # If user picks rock
        elif choice.lower().strip() == "rock" and comp_choice == "paper":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou lose!\n")
            comp_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            
        elif choice.lower().strip() == "rock" and comp_choice == "scissors":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou win!\n")
            p_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            


        # If user picks paper
        elif choice.lower().strip() == "paper" and comp_choice == "scissors":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou lose!\n")
            comp_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")

        elif choice.lower().strip() == "paper" and comp_choice == "rock":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou win!\n")
            p_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")


        # If user picks scissors
        elif choice.lower().strip() == "scissors" and comp_choice == "rock":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou lose!\n")
            comp_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")

        elif choice.lower().strip() == "scissors" and comp_choice == "paper":
            print(f"You chose: " + choice.strip().title())
            print(f"Computer chose: " + comp_choice.title())
            print("\nYou win!\n")
            p_count += 1
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")


        # If user picks quit
        elif choice.lower().strip() == "i quit":
            print(f"Score is: \n" + f"You: {p_count}" + f"\nComputer: {comp_count}" + f"\nTie: {tie_count}")
            print("\nThanks for playing! Goodbye!")
            break


        print("==========================================================================")


the_game()

