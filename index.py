import os
from random import randint
import random

# initiate commits per day and its weight  
# sampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
sampleList = [0, 1, 2, 3, 4]
dayInitial = 950
repeat = 5

def commit(dayStart, dayEnd, randomList):
     # main program
    for i in range(dayStart, dayEnd):

        print("day start: " + str(dayStart))
        print("day end: " + str(dayEnd))
        print("day: " + str(i))
        print(randomList)
        arrayIndex = i - dayStart

        # commit each day
        for j in range(0, randomList[arrayIndex]):
            
            print("counting commit:" + str(j))

            d = str(i) + 'days ago'

            print(d)

            with open('file.txt', 'a') as f:
                f.write(d)
            os.system('git add .')
            os.system('git commit -m "commit" --date="' + d + '"')
        os.system('git push origin master')


for count in range(0, repeat):

    # edit weight here
    # randomList = random.choices(
    #     sampleList, weights=(165, 5, 25, 30, 35, 35, 35, 35, 15, 15, 25, 15, 5, 5, 3, 3, 5), k=17)
    randomList = random.choices(
        sampleList, weights=(165, 5, 25, 30, 35), k=5)
    print("count: " + str(count) + "randomList: " + str(randomList))

    # first day
    if(count == 0):
        dayStart = dayInitial
        dayEnd = dayInitial + randomList.__len__()
        # start commit
        commit(dayStart, dayEnd, randomList)
    # repeat
    else:
        dayStart = dayInitial + randomList.__len__()
        print("start from " + str(dayStart))
        dayEnd = dayStart + randomList.__len__()
        # start commit
        commit(dayStart, dayEnd, randomList)