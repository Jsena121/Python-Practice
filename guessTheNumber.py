#this is a guess the number game
import random
secretNumber = random.randint(1,20)
print ('I am thinking of a number between 1 and 20')

#ask the player to guess six times
for guessesTaken in range (1,7):
    print ('Take a guess')
    guess = input()
    if int(guess) <secretNumber:
        print ('Your guess was too low')
    elif int(guess) > secretNumber:
        print ('Your guess was too high')
    else:
        break #This condition is the correct guess!
if int(guess) == secretNumber:
    print ('Good job! You guessed my number in ' +str(guessesTaken)+ ' guesses!')
else:
    print ('Nope. The number I was thinking of was ' +str(secretNumber) +'.')
