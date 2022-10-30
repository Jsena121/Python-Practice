def collatz(number): #defines the function
    if number % 2 == 0: #identifies even numbers
        return number//2
    elif number % 2 ==1: #identifies odd numbers
        return 3 * number + 1

print ('Enter number:')

while True: #begins the main loop
    try:
        yourNumber = int(input())
    except ValueError: #error message for non-integer inputs
        print ('Error: Input must be an integer')
        continue
    while yourNumber !=1: #collatz sequence will continue evaluating until reaching 1.
        yourNumber = collatz(yourNumber)
        print (yourNumber)
