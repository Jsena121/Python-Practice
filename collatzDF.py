import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def collatz(number):  # performs the collatz sequence
    if number % 2 == 0:  # identifies even numbers
        return number // 2
    elif number % 2 == 1:  # identifies odd numbers
        return 3 * number + 1

def counter(number): #counts number of steps for each number
    steps = []
    while number != 1:
        number = collatz(number)
        steps.append(number)
    return len(steps)

#Prompts input
runningTotal = []
print ('This script determines the maximum number of Collatz sequences needed to evaluate to 1 in a given range.')
print ('The script will automatically start at 1. How high do you wish to go?')
while True:
    try:
        maxCollatzRange = int(input())+1
        break
    except ValueError:
        print ('Error: Input must be an integer')
        continue

dfCollatz = pd.DataFrame(np.arange(1,maxCollatzRange),columns=['integer'])
dfCollatz['steps'] = dfCollatz['integer'].apply(counter)

print('The maximum number of steps to evaluate to 1 occurs at:')
print(dfCollatz[dfCollatz['steps']==dfCollatz['steps'].max()])
sns.scatterplot(data=dfCollatz,x='integer',y='steps',alpha=.05,edgecolor=None)
plt.show()
