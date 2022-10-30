import sys

while True:
    print('Type "Exit" to exit')
    response = input()
    if response == "Exit":
        sys.exit()
    else:
        print("please try again")
print("You typed " + response + ".")
