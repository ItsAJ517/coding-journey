# Music Game

# How to run: for this program, download all the files in this folder before running. Make sure all your downloaded files are in the same folder.

# Import modules
import csv, random, time

### FUNCTIONS ###

def extractData(file_name):
    with open(file_name, 'r') as file:
        read_data = csv.reader(file)
        data = list(read_data)

    return data

def writeData(file_name, data):
    with open(file_name, 'w', newline='') as file:
        to_write = csv.writer(file)

        for row in data:
            to_write.writerow(row)
        

### END FUNCTIONS ###

# Extract data
login_details = extractData('login_details.csv')
songs = extractData('songs.csv')
scores = extractData('scores.csv')


# Enter details
name = input("Name: ")
password = input("Password: ")

incorrect = 0
not_found = True

# LOGIN
for i in range(1, len(login_details)):
    # Check name
    if login_details[i][0] == name:
        not_found = False
        # Check password
        while login_details[i][1] != password:
            print("Password incorrect.")
            incorrect += 1
            # Ask if user wants to change their password
            if incorrect == 3:
                change = input("Would you like to change your password? [Y/n]: ").lower()

                # Change password
                if change == "y":
                    password = input("Enter your new password: ")
                    login_details[i][1] == password
                    print("Password changed succesfully.")
                    break
                
                # Exit program
                else:
                    exit()

            password = input("Password: ")
                
        print("Password authenticated.")
        break
    

# Add new details
if not_found:
    login_details.append([name, password, 0])
    print("Details added.")



print("Music Quiz")

access = True

# Main program begins here
while access:
    # Enter option
    option = input("""\nEnter 1. Play game
      2. Change name
      3. Change password
      4. Delete account
      5. View top 5 scores
      6. View your top 5 scores
      0. Exit
Option: """)

    #[1] Play Game
    if option == "1":
        # Initialize variables
        songs_copy = songs.copy()
        songs_copy.pop(0)
        score = 0
        correct = True
        
        while len(songs_copy) > 0 and correct:
            # Initialize song and artist
            song_data = random.choice(songs_copy)
            songs_copy.remove(song_data)

            artist = song_data[0]
            song = song_data[1]

            song_words = song.split()

            # Print details
            print("\nArtist:")
            print(artist)

            print("Song:")
            for i in range(len(song_words)):
                print(song_words[i][0], end = " ")

            print()

            attempts = 0

            # Guessing begins here
            while attempts <= 2:
                guess = input("Enter your guess for the song: ").lower()
                attempts += 1

                # Correct guess
                if guess == song.lower():
                    if attempts == 1:
                        score += 3
                        print("Correct! 3 points have been added to your score.")
                        
                    else:
                        score += 1
                        print("Correct! 1 point has been added to your score.")

                    attempts = 3

                # Incorrect guess
                else:
                    if attempts == 1:
                        # Hint system
                        hint = input("Incorrect. Would you like a hint? [Y/n]: ").lower()

                        if hint == 'y':
                            for i in range(len(song_words)):
                                if len(song_words[i]) > 1:
                                    print(song_words[i][0] + song_words[i][1], end = " ")
                                else:
                                    print(song_words[i][0], end = " ")

                            print()
                                    
                    else:
                        correct = False
                        attempts = 3

                        
        if correct:
            print("Congratulations! You got a perfect score!")
        else:
            print(f"Incorrect. The song was: {song}")
            

        # Final score
        print(f"Final score: {score}")

        # Store name + score and sort it
        for i in range(len(scores)):
            if len(scores) == 0:
                scores.append([name, score])
                break
            
            else:
                if score >= int(scores[i][1]):
                    scores.insert(i, [name, score])
                    break

                if i == len(scores)-1:
                    scores.append([name, score])

        

    #[2] Change name
    elif option == "2":
        for i in range(1, len(login_details)):
            if login_details[i][0] == name:
                name = input("Enter your new name: ")
                login_details[i][0] = name
                print("Name changed succesfully.")

    #[3] Change password
    elif option == "3":
        for i in range(1, len(login_details)):
            if login_details[i][1] == password:
                password = input("Enter your new password: ")
                login_details[i][1] = password
                print("Password changed succesfully.")

    #[4] Delete account
    elif option == "4":
        y = False
        for i in range(1, len(login_details)):
            if login_details[i][0] == name:
                time.sleep(1)
                delete = input("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT? [Y/n]: ").lower()

                if delete == "y":
                    print("Account deleted.")
                    y = True
                    break
                else:
                    print("Delete cancelled.")

        if y:
            login_details.pop(i)
            access = False

    #[5] View high scores
    elif option == "5":
        print("\nHere are the top 5 scores:")

        for i in range(len(scores)):
            if i < 5:
                print(f"{i+1}. {scores[i][0]} - {scores[i][1]}")

    #[6] User views their own top 5 scores
    elif option == "6":
        scores_printed = 1

        print("Here are your top 5 scores:\n")
        
        for i in range(len(scores)):
            if scores_printed > 5:
                break
            else:
                if scores[i][0] == name:
                    print(f"{scores_printed}. {scores[i][1]}")
                    scores_printed += 1

    #[0] Exit
    elif option == "0":
        access = False

    #[X] Invalid choice
    else:
        print("Invalid choice")


# Edit login details and scores
writeData('login_details.csv', login_details)
writeData('scores.csv', scores)


input("\nPress <Enter> to exit")



