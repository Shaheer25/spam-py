import random
from words import words
import string

def get_valid_word(word):
    word=random.choice(words)
    while '-' in word or  '' in word:
        word =random.choice(words)

    return word


def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alpabets=set(string.ascii_uppercase)
    used_letters=set()
    
    lives=6   # this lives at last


    while len(word_letters)>0 or lives>0:
        print('you ve used letters join', ''.join(used_letters)) # lives to here


             

    user_letter=input('input your letter').upper()
    if user_letter in alphabet -used_letter:
        used_letter.add(user_letters)
        if user_letter in word_letters:
            word_letters.remove(user_letters)
        else :
            lives=lives-1
            print("the guessed letter not in word")
            print("You've "+lives)
    
    elif user_letter in used_letters:
        print("You have already used this letters")
    else:
        print("Incorrect character")

if lives== 0:
    print("youve died")
else:
    print("yey yove won")


print(hangman())