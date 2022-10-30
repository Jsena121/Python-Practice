import random

wins = 0
losses = 0
ties = 0

#main game loop
while True:
    print (str(wins)+ ' wins, '+str(losses)+' losses, '+str(ties)+' ties')
    print ('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
    yourMove = input()
    if yourMove == 'r':
        print ('ROCK versus...')
    elif yourMove == 'p':
        print ('PAPER versus...')
    elif yourMove == 's':
        print ('SCISSORS versus...')
    elif yourMove == 'q':
        break
    else:
        print ('Not a valid input, please try again.')
        continue
    compMoveInt = random.randint(1,3)
    if compMoveInt == 1:
        compMove = 'r'
        print ('ROCK')
    elif compMoveInt == 2:
        compMove = 'p'
        print ('PAPER')
    else:
        compMove = 's'
        print ('SCISSORS')
    if yourMove == 'r':
        if compMove == 'r':
            print ('It is a tie!')
            ties = ties + 1
        elif compMove == 'p':
            print ('You lose!')
            losses = losses +1
        else:
            print ('You win!')
            wins = wins+1
    elif yourMove == 'p':
        if compMove == 'r':
            print ('You win!')
            wins = wins +1
        elif compMove == 'p':
            print ('It is a tie!')
            ties = ties +1
        else:
            print ('You lose!')
            losses = losses+1
    else:
        if compMove == 'r':
            print ('You lose!')
            losses = losses+1
        elif compMove == 'p':
            print ('You win!')
            wins = wins +1
        else:
            print ('It is a tie!')
            ties = ties +1


