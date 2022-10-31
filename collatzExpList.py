import numpy as np

def collatz(number):  # defines the function
    if number % 2 == 0:  # identifies even numbers
        return number // 2
    elif number % 2 == 1:  # identifies odd numbers
        return 3 * number + 1

runningTotal = np.array([0])
#currentRow = [[0],[0]]
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
    while collatzInp != 1:
        collatzInp = collatz(collatzInp)
        #print (i)
        count = count + 1
        if collatzInp == 1:
            #currentRow = np.array([i,count])   Lines 23 and 24 give a 2-column array
            #runningTotal = np.vstack((runningTotal,currentRow))
            currentRow = np.array([count]) #only one column is needed since i will be the index
            runningTotal = np.vstack((runningTotal,currentRow))
    #resultTable = print (np.vstack([[i],[count]]))  #<--- works
    #print ([[i],[count]]) #works
    #runningTotal = ([[i],[count]])
    #resultTable = np.vstack(resultTable)
    #resultTable = np.vstack([[i],[count]])

    #resultTable = ([[i],[count]])
    #resultTable = np.vstack(resultTable)

#results
print (runningTotal)
highestCount = max(runningTotal)
highestCountInd = np.array([index for index in range(len(runningTotal)) if runningTotal[index] == highestCount])
highestCountOcc = highestCountInd + 1 #needed to shift indeces up by 1 to give i value
print ('The greatest number of Collatz sequences needed to return 1 from positive integers 1 through ' +str(i)+ ' is '+str(highestCount)+'.')
print ('The number(s) at which this occurs is/are: '+str(highestCountOcc))


#print (runningTotal.argmax(axis=0)+1)    works in showing index for highest count
#maxCollatzRow = np.argmax(np.max(runningTotal,axis=1))+1
#maxCollatzColumn = max(np.max(runningTotal,axis=1))
#print (maxCollatzRow)
#print (maxCollatzColumn)
