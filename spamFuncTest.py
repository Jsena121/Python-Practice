def spam(bacon): #bacon is a parameter
    return 31337
eggs = True
bacon = spam(eggs) #bacon is global variable; this line calls the spam(bacon) function and passes the eggs variable to the bacon parameter
print (bacon)

def blah ():
    print (bacon) #global variables can be used in local scope

blah()
