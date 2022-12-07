# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

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

rev_lst=lst[::-1]                 #Перевернула список
print(rev_lst)


for j in range(len(lst)):
    for k in range(len(rev_lst)):
        if ((len(lst)%2 == 0)and(len(rev_lst)%2 == 0))and(j==k):
            res = lst[j]*rev_lst[k]
            print(res)
            
      
