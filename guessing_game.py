# Guessing Game

import random
from english_words import get_english_words_set

web2lowerset = get_english_words_set(['web2'], lower=True)

comp_score = 0
my_score = 0
score_tally = f"Computer: {comp_score}, My Score {my_score}"

happy = "    _________   \n   / __   __ \  \n  /  <>   <>  \  \n /      \/     \ \n|               |\n|    \      /   |\n \    \____/   / \n  \           /  \n   \_________/  "
oh_no = "    _________   \n   / /     \ \  \n  /   x    x  \  \n /      \/     \ \n|               |\n|      /--\     |\n \     \__/    / \n  \           /  \n   \_________/  "


def choose_word():
    return random.choice(list(web2lowerset))


def game(word):
    global my_score
    global comp_score
    global happy
    global oh_no
    print(f"My Score: {my_score}, Comp Score: {comp_score}")
    print(happy)
    hidden_word = []
    turns_left = 10
    letters_guessed = []
    for letter in word:
        hidden_word.append("_")
    print("What is this word? " + "".join(hidden_word))
    print("You have " + str(turns_left) + " turns to guess the word")
    guess = input("guess a letter: ")
    letters_guessed.append(guess)

    while "".join(hidden_word) != word and turns_left > 0:
        turns_left -= 1
        if guess == word:
            print(f"!!!!!!!!! Yay you did it! The word was {word} !!!!!!!!!!")
            print(happy)
            my_score += 1
            return start_game()
        elif guess in word:
            print(f"Good job, '{guess}' is in the word")
            print(happy)
            for index, char in enumerate(word):
                if char == guess:
                    hidden_word[index] = char
            print("".join(hidden_word))
            print(
                f"Letters guessed: {letters_guessed}, Turns Left: {turns_left}")
            if "".join(hidden_word) == word:
                print(
                    f"!!!!!!!!! Yay you did it! The word was {word} !!!!!!!!!!")
                print(happy)
                my_score += 1
            else:
                guess = input("guess a letter: ")
                letters_guessed.append(guess)
        else:
            print("********** Guess again... *********")
            print(oh_no)
            print(
                f"Letters guessed: {letters_guessed}, Turns Left: {turns_left}")
            print("".join(hidden_word))
            guess = input("guess a letter: ")
            letters_guessed.append(guess)
    comp_score += 1
    print(f"************* You lose! The word was + {word} ***************")
    print(oh_no)
    start_game()


def start_game():
    random_word = choose_word()
    initialize = input("Would you like to play? (y/n)")
    if initialize == "y":
        game(random_word)
    elif initialize == "n":
        return print("Ok Bye!")
    else:
        print("Please type either 'y' or 'n'")
        start_game()


start_game()


#     _________
#    / /     \ \
#   /   x   x   \
#  /      \/     \
# |               |
# |      /  \     |
#  \     \__/    /
#   \           /
#    \_________/
