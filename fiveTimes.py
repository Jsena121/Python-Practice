#for loop
print ('My name is')
for i in range (5):
    if i == 3:
        continue
    print ('Jimmy Five Times ('+str(i)+')')

#identical for loop using while
print('My name is')
i=0
while i<5:
    print ('Jimmy Five Times ('+str(i)+')')
    i=i+1

#find sum of numbers 1 through 101
total = 0
for num in range (101):
    total = total + num
print (total)
