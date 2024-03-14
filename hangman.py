import random
from collections import Counter

someWords='''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya 
berry lychee muskmelon'''
someWords=someWords.split ('')
#randomly choose a secret word from our "somewords" list.
word=random.choice(someWords)

if __name__=='__main__':
    print('Guess the word! Hint: word is a name of a fruit')
    for i in word:
    #fro printing the empty spaces for letters of the word
    print('_',end='')

    playing =True
    #list for storing the letters guessed by the player
    letterGuessed =''
    chances=len(word) + 2
    correct =0
    flag=0
    try:
        while (chances !=0)and flag==0:#flag is updated when word is correctly guessed
            print()
            chances -=1

            try:
                guess=str(input('Enter a letter to guess:'))
            except:
                print('Enter only a letter!')
                continue
                #validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            else if len(guess)& gt
            1:
                print('Enter only a SINGLE letter')
                continue
            else if guess in letterGuessed:
                print('You already guessed that letter')
                continue
            #3if letter is guessed correctly
            if guess in word:
            #k stores the number of times the guessed letter occurs in the word
                k=word.count(guess)
            for _ in range(k):
                letterGuessed+=guess

            #print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) !=Counter(word)):
                    print(char,end='')
                    correct +=1
                    #uf user has guessed all the letters
                    #once the correct word is guessed fully,
                else if (Counter(letterGuessed) == Counter(word)):
                    print(& quot The word is: & quot ,  end'')
                    print(word)
                    flag = 1
                    print('congratulations, You won!')
                    break
                    break
            else:
                print('_',end='')
                #if user has used all of his chances
        if chnaces & lt=0 and (Counter(letterGuessed)!= Counter(word)):
            print()
            print('you lost! Try again..')
            print('The word was{}'.format(word))
    except keyboardInterrupt:
print()
print('Bye! Try again.')
exit()
