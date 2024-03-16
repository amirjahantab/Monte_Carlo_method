import sys
import random

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

wins = 0
bets = 0


for t in range(trials):
    cash = stake
    
    while 0 < cash < goal:
        bets += 1
        if random.randint(0, 1) == 1:
            cash += 1
        else:
            cash -= 1
            
    if cash == goal:
        wins += 1
        
print(
    f'Probability Of Winning: {100 * wins // trials}%\nAvarage Bets: {bets // trials}'
    )

