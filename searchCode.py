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

# produce menu number, code selection for item, first code location to test against and first code segment
def OldEnglish(choice, codeLocation, codeValue):
    print("")
    print("You remove the painting from the wall and read the note.")
    if choice == codeLocation:
        print("In the note, you see a number " + str(codeValue) + ".")
    else:
        print("You find no code.")
        print("")

def FlowerPot(choice, codeLocation, codeValue):
    print("")
    print("A dark green flower pot holds roses that seem to have died long ago.")
        if choice == codeLocation:
                print("On the base of the flower pot, you see the number " + str(codeValue) + ".")
                print("")
        else:
                print("You find nothing on the side of the pot. It is plain.")
                print("")
