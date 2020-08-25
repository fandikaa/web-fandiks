import os
from random import randint
import random

# initiate commits per day and its weight  
sampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

dayInitial = 750
repeat = 10

for count in range(0, repeat):
    randomList = random.choices(
        sampleList, weights=(165, 5, 25, 30, 35, 35, 35, 35, 15, 15, 25, 15, 5, 5, 3, 3, 5), k=17)
    print("count: " + str(count) + "randomList: " + str(randomList))

    dayStart = dayInitial
    dayEnd = dayStart + randomList.__len__()

    # repeat preparation
    if(count != 0):
        dayStart = dayInitial + randomList.__len__()
        print("start from " + str(dayStart))
        dayEnd = dayStart + randomList.__len__()

    # main program
    for i in range(dayStart, dayEnd):
        print(randomList)
        arrayIndex = i - dayStart
        for j in range(0, randomList[arrayIndex]):
            d = str(i) + 'days ago'
            with open('file.txt', 'a') as f:
                f.write(d)
            os.system('git add .')
            os.system('git commit -m "commit" --date="' + d + '"')
        os.system('git push origin master')