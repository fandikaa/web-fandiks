import os
from random import randint

for i in range(1, 365, randint(0, 3)):
    for j in range(0, randint(0, 10)):
        d = str(i) + 'days ago'
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit -m "commit" --date="' + d + '"')

os.system('git push origin master')

# The above script will create a file.txt file and commit it to the repository.
# The commit date will be set to the number of days ago.
# The number of commits will be random.