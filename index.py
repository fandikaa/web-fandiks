import os
from random import randint


import random
  
sampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
randomList = random.choices(
  sampleList, weights=(135, 5, 15, 35, 35, 35, 35, 35, 30, 25, 25, 15, 15, 5, 5, 5, 5), k=17)
  
# print(randomList)


for i in range(450, 463):
    for j in range(sampleList[0], sampleList[15]):
        d = str(i) + 'days ago'
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit -m "commit" --date="' + d + '"')
    os.system('git push origin master')



# The above script will create a file.txt file and commit it to the repository.
# The commit date will be set to the number of days ago.
# The number of commits will be random.