import random

def randomx(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number :
        guess=  int (input(f"Enter a number {x}"))
        if guess<random_number:
            print("Its low Choose higher")
        elif guess>random_number:
            print("its higher")
    print("CORRECT congrsts")


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c' :
        if low!=high:
         guess=random.randint(low, high)
        else:
          low=guess
        feedback=input(f'the number {guess} is higher H lower L or correct C').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
         low=guess+1
         
    
    print("YEY The computer guessed correctly")

computer_guess(1000)


