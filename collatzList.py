def collatz(number):  # defines the function
    if number % 2 == 0:  # identifies even numbers
        return number // 2
    elif number % 2 == 1:  # identifies odd numbers
        return 3 * number + 1

#Prompts input
runningTotal = []
print ('This script determines the maximum number of Collatz sequences needed to evaluate to 1 in a given range.')
print ('The script will automatically start at 1. How high do you wish to go?')
while True:
    try:
        maxCollatzRange = int(input())
        break
    except ValueError:
        print ('Error: Input must be an integer')
        continue

#counts how many repetitions of the sequence are needed in a selected range to get to 1
for i in range(1, maxCollatzRange+1): #counts from 1 to number selected by user
    collatzInp = i
    count = 0 #counts repetitions of the collatz function
    if i == 1:
        runningTotal.append(count)
        continue
    while collatzInp != 1:
        collatzInp = collatz(collatzInp)
        count += 1
        if collatzInp == 1:
            runningTotal.append(count)

#results
#print (runningTotal)  #Python prints the entire list, unlike when it printed a short
                        #version of the array. Printing this will cause significant
                        #slowdown!
highestCount = max(runningTotal)

#This creates a list to account for repeated instances of the highest count. It is probably
#unnecessary. Counting through 1000000, there has not yet been a repeated count number.
highestCountOcc = []
for index in range (len(runningTotal)):
    if runningTotal[index] == highestCount:
        highestCountOcc.append(index + 1)
#More succinct version below, but it does not search for repeated highest counts.
#highestCountOcc = runningTotal.index(highestCount) + 1
print ('The greatest number of Collatz sequences needed to return 1 from positive integers 1 through ' +str(i)+ ' is '+str(highestCount)+'.')
print ('The number(s) at which this occurs is/are: '+str(highestCountOcc))
