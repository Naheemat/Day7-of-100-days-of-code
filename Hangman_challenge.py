import random

#import 'word_list' from the module 'Hangman_words'.
from Hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Importing logo from 'Hangman_art.py' 
from Hangman_art import logo
print(logo)


#Creating blanks using underscore 
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}, Enter another letter")

    #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #To Check if the user is wrong.
    if guess not in chosen_word:
        #prints out the wrong letter and let the user know it's not in the chosen_word,
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The solution is {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    #Importing the stages from 'Hangman_art.py' 
    from Hangman_art import stages
    print(stages[lives])

