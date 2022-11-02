message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
characterCount = 0
for character in message:
    count.setdefault(character,0)
    #characterCount +=1 #manually counts the length of the string
    count[character]+=1
    #print(character) #variable character equates to each letter as it cycles through

print(count)
highestCount = max(count.values())
highestCountCharIndex = list(count.values()).index(highestCount)
highestCountChar = list(count.keys())[highestCountCharIndex]
#print (characterCount)

print('The following string has ' + str(len(message)) + ' characters: \n' + message)
print('')

print('The breakdown for the number of instances each character appeared are as follows')
for k, v in count.items():
    print ('For the character, "' +str(k)+'", there is/are ' +str(v) +' instance(s).')

print('The most common character was "' + str(highestCountChar) + '" with ' +str(highestCount) + ' occurrences.')
