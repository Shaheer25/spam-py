import random

def play():
    user=input("'R' for rock'P' for paper and 'S' for scissors")
    computer=random.choice(['r','p','s'])

    if user==computer:
       return 'its a tie'
    
    if win(user,computer):
        return 'you win'
 
    return 'you loose'


def win(player,opponent):
    if (player=='r' and opponent=='s') or  (player=='p' and opponent=='r') or  (player=='s' and opponent=='p'):
        return True
print(play())
