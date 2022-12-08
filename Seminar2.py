# Задать список из строк. Проверить, присутствует ли в списке число.

lst = ['blue', 'r3d','gre2n', 'hello']
f = False
for i in range(len(lst)):
    if "2" in lst[i]:
        f = True
        break
print(f)