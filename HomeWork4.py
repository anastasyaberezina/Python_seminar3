# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Здесь не поняла, получился ли у меня список Фибоначчи, или это чтото другое.

num = int(input('Введите число '))

def Fib(numb):
    lst = []
    x, y = 1, 1
    for i in range(numb-1):
        lst.append(x)
        x=y
        y+=x
    x, y = 0, 1
    for i in range(numb):
        lst.insert(0, x)
        x=y
        y=x-y
        return lst

lst=Fib(num)
lst2=lst[::-1]
res=[-x for x in lst2]
result_lst=res+Fib(num)
print(result_lst)


