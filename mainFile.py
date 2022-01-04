import random
import introduction import intro
from menu import menu
from searchCode import Chest, FlowerPot, OldEnglish

code1 = random.randint(0,9)
code2 = random.randint(0,9)
code3 = random.randint(0,9)
code = int(str(code1) + str(code2) + str(code3))
items = ["OldEnglish","FlowerPot","Chest"]
code1Location = random.randint(0, 1)
code2Location = random.randint(1, 2)
code3Location = random.randint(0, 2)

intro()
# initiate game loop
while True:
    # call menu and place in variable
    choice = menu("What do you want to look at in the room? ")
    # send the choice number and the code location to see if item in right location. none item related will be sent to door lock
    if choice == 1:
        OldEnglish(choice, code1, code1Location)
    elif choice == 2:
        FlowerPot(choice, code2, code2Location)
    elif choice == 3:
        Chest(choice, code3, code3Location)
    else
        result = Door(code)
    if result == 1:
        break
