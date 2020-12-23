import os
from random import randint
import random

# initiate commits per day and its weight  
sampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
randomList = random.choices(
  sampleList, weights=(145, 5, 15, 35, 35, 35, 35, 35, 30, 25, 25, 15, 15, 5, 5, 5, 5), k=17)

# initiate n days before
dayStart = 630
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