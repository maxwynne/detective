def Door(code):
    print("The door's padlock contains three digits. You enter a code")
    while True:
        try:
                option1 = int(input("Digit one: "))
                break
        except:
                print("Your first digit must be a number between 0-9:")

    while True:
        try:
                option2 = int(input("Digit two: "))
                break
        except:
                print("Your second digit must be a number between 0-9:")

    while True:
        try:
                option3 = int(input("Digit three: "))
                break:
        except:
                print("Your third digit must be a number between 0-9:")
    digitCode = int(str(option1)) + str(option2) + str(option3))
    print("")
    if digitCode == code:
            print("You hear a click. You entered the right code. The door unlocks")
            return(0)
