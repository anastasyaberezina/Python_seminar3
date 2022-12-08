# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

res = 1
lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
ask = "qwe"
count = 0

for i in range(len(lst)):
    if lst[i] == ask:
        count +=1
    if count == 2:
        res = i
        break
print(res)