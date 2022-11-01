import random

def streakFinder(coinFlipResults):
    currentStreak = 0
    totalStreaks = 0
    for result in range(len(coinFlipResults)):
        #if coinFlipResults[result]==coinFlipResults[result+1]==coinFlipResults[result+2]==\
         #  coinFlipResults[result+3]==coinFlipResults[result+4]==coinFlipResults[result+5] \
          # ==coinFlipResults[result+6]:   long way
        if result == 0:
            pass
        elif coinFlipResults[result] == coinFlipResults[result-1]:
            currentStreak +=1
        else:
            currentStreak = 0
        if currentStreak == 6: #added variable currentStreak stops only counts a streakFinder
                                #once it hits 6. The other methods added an entire streak when
                                #one streak extended beyond 6.
            totalStreaks +=1
    return totalStreaks
        #if coinFlipResults[result:result+6] == ['H','H','H','H','H','H']:
           # streaks+=1
           # result+=10
        #elif coinFlipResults[result:result+6] == ['T','T','T','T','T','T']:
           # streaks+=1
           # result+=10


numberOfStreaks = 0
for experimentNumber in range (10000):
    headsOrTails = []
    for coinFlip in range (100):
        if random.randint(0,1) == 0:
            headsOrTails.append('H')
        else:
            headsOrTails.append('T')
    numberOfStreaks += streakFinder(headsOrTails)

#test = ['T', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'H']
#numberOfStreaks = streakFinder(headsOrTails)
print (numberOfStreaks)
print (headsOrTails)

print ('Chance of streak: %s%%' %(numberOfStreaks / 10000))

