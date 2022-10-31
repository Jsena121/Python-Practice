#Uses for and while loops to separate a list based on data type

spam = [1, 2, 5, 100, 1000, "cat", "bat", "rat", "elephant"]

stringSpam = []
for i in range(len(spam)):
    if spam[i] == str(spam[i]):
        stringSpam.append(spam[i])
        spam[i] = 0
    #if spam[i] == str(spam[i]): gives error message likely bc this changes size of spam
        #spam.remove(spam[i])    and makes i extend out of range
while True: #infinite while loop allows for 0 values to continually be removed
    try:
        spam.remove(0)
    except ValueError: #except statement breaks the otherwise infinite loop once there are no more 0s
        break
print(spam)
print('Strings removed were: ')
print (stringSpam)
