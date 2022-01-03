import random
import time
def displayIntro():
    print('Last night, you went to sleep.')
    print('You woke up in an unfamiliar environment.')
    print('You begin to inspect your surroundings,')
    print('there is an Old English painting and a chest of draws.')
    print('Both look off to you. You begin to inspect')

    print('1 - to check the Old English painting')
    print('2 - to go through the chest of draws')

while True:
    englishOrDraws = input()
    try:
            if int(englishOrDraws) == 1:
                print('Behind the painting, you feel a note. But you cannot examine it.')
                print('You go through the chest of draws and find a notebook.')
                break
            elif int(englishOrDraws) == 2:
                print('You rifle through the draws and find a notebook.')
                print('You also identify a note behind the Old English painting.')
            else:
                print('Enter either 1 or 2 to proceed:')
    except:
            print('You must press either 1 or 2:')
