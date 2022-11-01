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

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []
print(list2String(spam))
