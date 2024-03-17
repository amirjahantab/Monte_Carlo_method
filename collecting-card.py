import random
import sys

trials = int(sys.argv[1])

SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace')

deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck += [card]
        

s = []
for i in range(trials):
    check = {
    'Clubs': False,
    'Diamonds': False,
    'Hearts': False,
    'Spades': False,
    }
    
    count = 0
    while True:
        if check['Clubs'] and check['Diamonds'] and check['Hearts'] and check['Spades']:
            s += [count]
            break                
        
        random_card = random.choice(deck)
                
        if 'Clubs' in random_card:
            check['Clubs'] = True
        elif 'Diamonds' in random_card:
            check['Diamonds'] = True
        elif 'Hearts' in random_card:
            check['Hearts'] = True
        else:
            check['Spades'] = True

        count += 1

print(sum(s)//len(s))