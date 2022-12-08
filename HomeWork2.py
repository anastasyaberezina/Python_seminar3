# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


lst = [1.1, 1.2, 3.1, 5.1, 10.01]

for i in range(len(lst)):
    lst[i] = lst[i]%1
    res=round(lst[i], 2)
    print(res)
    res=str(res)

    if res == float:
        

        for j in range(len(res)):
            min=res[0]
            max=0
            if res[j]>max:
                max=res[j]
                min=max
            else:
                max=max
                min=res[j]
        print(max,min)            

