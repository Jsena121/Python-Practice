def list2String(inputList):
    resultString = ''
    for x in range(len(inputList)):
        if x != len(inputList)-1 and len(inputList)!=0:
            resultString += str(inputList[x]) + ', '
        elif x == len(inputList) - 1 and len(inputList) !=0 and len(inputList)!=1:
            resultString += 'and ' + str(inputList[x])
        elif len(inputList) == 1:
            resultString = str(inputList[x])
    return resultString

catNames = []
while True:
    print ('Enter the name of cat ' + str(len(catNames)+1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    #catNames = catNames + [name] #list concatenation
    catNames.append(name) #same result using append method
print ('The cat names are ' + list2String(catNames)+ '.')
