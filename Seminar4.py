#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def Random_numb (first = 0, last = 100):
    import time
    time.sleep(0.01)
    ran = int(str(time.time())[-3:])
    while True:
        if ran<first:
            ran+=(last-first)
        if ran>last:
            ran-=(last-first)
        if first<=ran<=last:
            return ran      

lst = []                          #Заполнила список случайными числами
for i in range(10):
    lst.append(Random_numb(1, 9))

print(lst)   

# Вариант 1:

sum=0
for i in range(len(lst)):
    if i%2==1:
        sum+=lst[i]

print(sum)

# Вариант 2:

sum=0
for i in range(1, len(lst), 2):
        sum+=lst[i]

print(sum)


