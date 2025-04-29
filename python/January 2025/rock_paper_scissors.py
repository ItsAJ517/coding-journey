#Rock Paper Scissors
import random

# Choices
choices = ["rock", "paper", "scissors"]

### FUNCTIONS ###

def randomChoice():
    return random.choice(choices)


def userChoice():
    print("\nYour choices are:")

    for i in range(1, len(choices)+1):
        print(f"{i}. {choices[i-1]}")

    choice = input("Enter your choice: ").lower()
    
    while choice not in choices:
        print("Please enter a valid choice")
        choice = input("Enter your choice: ").lower()

    return choice



def compareChoices(choice1, choice2):
    #cases where player 1 wins
    if choice1 == "rock" and choice2 == "scissors":
        return "1"
        
    elif choice1 == "scissors" and choice2 == "paper":
        return "1"

    elif choice1 == "paper" and choice2 == "rock":
        return "1"

    #cases where choice 2 wins
    elif choice1 == "rock" and choice2 == "paper":
        return "2"

    elif choice1 == "paper" and choice2 == "scissors":
        return "2"

    elif choice1 == "scissors" and choice2 == "rock":
        return "2"

    #cases where it's a draw
    else:
        return "0"


### END FUNCTIONS ###


# Main game begins here
print("Welcome to Rock, Paper, Scissors!")

while True:
    # user enters game mode
    while True:
        option = input("""
Enter (1) Play against the computer
    (2) Computer A vs Computer B
    (3) Exit
    Option: """)

        if option in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice!")

    print()

    # break the loop if the user's option is 'exit' so that they don't get the 'best of' prompt
    if option == "3":
        break

    # best of...
    while True:
        best_of = input("""
Would you like to play a best of 1, 3, or 5?
Enter the number for your choice: """)

        # avoid invalid inputs
        if best_of not in ["1", "3", "5"]:
            print("Please enter a valid number")
        else:
            break
    
    #[1] Option 1: Player vs Computer
    if option == "1":
        # Variables for score and games played
        player_score = 0
        computer_score = 0
        games_played = 0
        
        while games_played < int(best_of):
            #Player and computer choices
            player_choice = userChoice()
            computer_choice = randomChoice()

            #Print both choices
            print(f"\nYour choice was {player_choice} and the computer's choice was {computer_choice}.")
            
            #Compare choices
            #[1.1] Player 1 wins
            if compareChoices(player_choice, computer_choice) == "1":
                print("You win this round!")
                player_score += 1 # increment score
                
                print(f"You: {player_score}\tComputer: {computer_score}") # print score of each player

                if player_score / int(best_of) > 0.5:
                    print("\nYou are the winner!")
                    break

                # games_played only incremented when someone wins so the loop keeps going and the 'best of' system is implemented properly
                games_played += 1
                
            #[1.2] Player 2 wins
            elif compareChoices(player_choice, computer_choice) == "2":
                print("The computer wins this round!")
                computer_score += 1 # increment score
                
                print(f"You: {player_score}\tComputer: {computer_score}") # print score of each player

                if computer_score / int(best_of) > 0.5:
                    print("\nThe computer is the winner!")
                    break

                games_played += 1

            #[1.3] It's a draw
            else:
                print("It's a draw!")
                print(f"You: {player_score}\tComputer: {computer_score}") # print score of each player


    #[2] Option 2: Computer A vs Computer B
    elif option == "2":
        #Variables for computer scores and games played
        computerA_score = 0
        computerB_score = 0
        games_played = 0
        
        while games_played < int(best_of):
            computerA_choice = randomChoice()
            computerB_choice = randomChoice()

            #Print both choices
            print(f"\nComputer A's choice is {computerA_choice} and Computer B's choice is {computerB_choice}.")

            #Compare choices
            #[2.1] Computer A wins
            if compareChoices(computerA_choice, computerB_choice) == "1":
                print("Computer A wins this round!")
                computerA_score += 1 #increment computer A score

                input(f"Computer A: {computerA_score}\tComputer B: {computerB_score}") #print each computers' score

                if computerA_score / int(best_of) > 0.5:
                    print("Computer A is the winner!")
                    break

                games_played += 1
                
            #[2.2] Computer B wins
            elif compareChoices(computerA_choice, computerB_choice) == "2":
                print("Computer B wins this round!")
                computerB_score += 1 #increment computer B score

                input(f"Computer A: {computerA_score}\tComputer B: {computerB_score}") #print each computers' score

                if computerB_score / int(best_of) > 0.5: #mathematical stuff
                    print("Computer B is the winner!")
                    break

                games_played += 1

            #[2.3] It's a draw
            else:
                print("It's a draw!")
                input(f"Computer A: {computerA_score}\tComputer B: {computerB_score}") #print each computer's score


    #Asking if user wants to play again
    play_again = input("Would you like to play again? [Y/n]: ").lower()

    #used for incorrect user inputs
    while play_again not in ["y", "n"]:
        print("Please enter a valid choice")
        play_again = input("Would you like to play again? [Y/n]: ").lower()

    if play_again == "n":
        break

input("Thanks for playing!")    
