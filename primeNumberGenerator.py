def primeNumber(number):
    for i in range (1,number+1):
        if number % i == 0 and i != 1 and i != number:
            return False
    else:
        return True


#Prompts input
print('This script outputs all prime numbers in a selected range, starting at 1.')
print('How high do you wish to go?')
while True:
    try:
        maxPrimeRange = int(input())
        break
    except ValueError:
        print ('Error: Input must be an integer')
        continue

primeNumberList = []
for i in range(1,maxPrimeRange + 1):
    primeTest = primeNumber(i)
    if primeTest == True:
        primeNumberList.append(i)
    else:
        continue

print(primeNumberList)
