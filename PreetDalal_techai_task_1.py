# Initially there were 2 files, logic.py and play.py (for better modularity), but I have combined these into a single file for ease of checking

# Importing the random library to choose a random word

import random

# It is time to build the game logic
# This includes the following: Setting max attempts, checking for validation, and showing 

def game_logic(user_input, answer_word):
    # Setting colors using ANSI escape codes

    GRAY = '\033[90m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    # Case when user has entered invalid word

    if(len(user_input) != 5):
        print("Please enter five-letter words only")
        return 0
    
    # Case when user input exactly matches our word

    elif(user_input == answer_word):
        print(GREEN+answer_word+RESET)
        return 1
        
    
    # Case when user input does not match our word

    else:

        # We must initialize a list of strings to be displayed

        display= [""]*5

        # answer_remaining variable has been declared so the we dont mark multiple occurences as yellow

        answer_remaining = list(answer_word)


        # Since we already checked for word length earlier, we know that user input is five characters

        for i in range(5):
            if(user_input[i] == answer_word[i]):
                display[i] = (GREEN + user_input[i] + RESET)
                answer_remaining[i] = None
            
        for i in range(5):
            if display[i] != "": # already green
             continue
            if(user_input[i] in answer_remaining):
                display[i] = (YELLOW + user_input[i] + RESET)

                # Now remove the first occurrence of this letter
                answer_remaining[answer_remaining.index(user_input[i])] = None

            else:
                display[i] = (GRAY + user_input[i] + RESET)
            
        
        print("".join(display))    
        return 2
    
# Now it is time to play the game
    
# Loading the .txt file in read mode

with open("valid-wordle-words.txt", 'r') as words_file:
    words = words_file.read().splitlines() # Now all the words have been saved in words

answer_word = random.choice(words)

attempts = 6        # Create an attempts variable with value 6

while(attempts):
    user_input = input(f"{7-attempts}. Enter a five-letter word: ").lower()
    case = game_logic(user_input,answer_word)

    if case == 1:
        break
    elif case == 2:
        attempts-=1

if attempts>0:
    print(f"You have won the game. The answer was {answer_word}")

else:
    print(f"You have lost the game. The answer was {answer_word}")






















