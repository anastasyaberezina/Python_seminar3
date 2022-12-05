#Алгоритм перемешивания списка

#import random

#lst = [1, 2, 3, 4, 6]
#print(lst)
#random.shuffle(lst)
#print(lst)

import time

def random_without_lib(x):
    return int(round(time.time() * 1000) % x)

lst = [1, 2, 3, 4, 5]    

for i in range(len(lst)):
    lst[i], lst[random_without_lib(len(lst))] = lst[random_without_lib(len(lst))], lst[i]

print(lst)    