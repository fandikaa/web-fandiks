import random
  
sampleList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
randomList = random.choices(
  sampleList, weights=(135, 5, 15, 35, 35, 35, 35, 35, 30, 25, 25, 15, 15, 5, 5, 5, 5), k=17)

print(randomList.__len__())