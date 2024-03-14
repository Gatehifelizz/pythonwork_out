import random

# library that we use in order to choose
# on random words from a list of words
name = input("what is your name")
# Here the user is asked to enter the name first
print("Good luck!", name)
words = ['reverse','rascal', 'wendigo', 'inshallah', 'come', 'wednesday','Kakamega', 'billionaire', 'lottery','rainbow','player','geeks']
# Function will choose one random word from this list
word = random.choice(words)
print("guess the characters")
guesses = ''
# Any number of turns can be used here
turns = 12

while turns > 0:
    # counts the number of times a user fails
    failed = 0
    # all characters from the input
    # word talking one at a time.
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed += 1
    if failed == 0:
        # user will win game if failure is 0 'you win' will be given as output
        print("You win")
        # this print the correct word
        print("The word is:", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess another character:")
    # every input character will be stored in the guesses
    guesses += guess
    # check input with character in word
    if guess not in word:
        turns -= 1
        # if the character doesn't match word
        # then "wrong" will be given as output
        print("wrong")

        # this will print the number of turns left for the user
        print("you have", +turns, 'more guesses')

        if turns == 0:
            print("you loose")
