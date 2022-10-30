def spam():
    global eggs
    eggs = 'spam' #this is the global. Code cannot use both local eggs and global eggs in the same function

def bacon ():
    eggs = 'bacon' #this is the locals

def ham():
    print (eggs) #this is the global

eggs = 42 # this is the global
spam()
print (eggs)
