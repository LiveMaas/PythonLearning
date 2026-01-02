# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random

word_list = ["cat", "dog", "whale", "fish", "shark","zebra","elephant"]
chosen_word = random.choice(word_list)
guess = input("Guess a leter: ").lower()
print(chosen_word)
for letter in chosen_word: 
    if letter == guess:
        print("correct")
    else:
        print("wrong")



    