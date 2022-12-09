# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Хотела решить чере %1, что то не вышло.

lst = [1.1, 1.2, 3.1, 5.1, 10.01]

for i in range(len(lst)): # Ищу дробную часть элеметов
    lst[i] = lst[i]%1
    res=round(lst[i], 2)
    print(res)

if res==float:
    for j in range(len(res)): # Запускаю поэлементный цикл 
    
        min=res[0]
        print(round(res[0], 2))
        max=0
        if res[j]>max:
            max=res[j]
            min=max  
        else:
            max=max
            min=res[j]
        break
    print(max-min)            

