name = ()
null = ()
wrong = 0
while True:
    if null == 1 or wrong == 5:
        break
    print("Who are you?")
    name = input()
    if name != "Joe":
        print("Go away, you're not Joe")
        continue
    else:
        print("Hello, Joe. What is the password? (Hint: it is a fish)")
    while True:
        if wrong != 0 and wrong < 5:
            print("You have "+ str(5- wrong)+ " attempts remaining")
        if wrong == 5:
            break
        password = input()
        if password == "I am not Joe":
            break
        elif password == "swordfish":
            null = 1
            break
        else:
            wrong = wrong + 1
            continue
if wrong == 5:
    print("Access Denied...")
else:
    print("Access granted.")
