# pass a list of items to choose from in a menu format
def menu(list, question):
    # for loop: print each item from list to be chosen
    for choice in list:
        print(list.index(choice), choice)
    # while loop to check input
    while True:
        result = input(question)
        try:
                result = int(result)
                break
        except:
                print("Selection must be between 0-9")

    return result
