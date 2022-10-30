def spam():
    print(eggs) #gives error unless line 3 is commented out
    eggs = 'spam local' #how does Python know about this assignment before running it?

eggs = 'global'
spam()
