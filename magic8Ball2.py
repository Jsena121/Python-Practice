import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate an ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print (messages[random.randint(0,len(messages)-1)])
#print (messages[random.randint(range(len(messages)))]) #does not work, output is range(0,9) rather
                                                        #than raw numbers required for randint
