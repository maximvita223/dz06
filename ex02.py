# Дан список чисел напишите программу возводящюю в квадрат элементы из списка

# lst = [1,2,3,4,5,10]
# lst1 = []
# for i in lst:
#     lst1.append(i**2)
# print(lst1)

lst = [1, 2, 3, 4, 5, 10]
lst = list(map(lambda x: x**2, lst))
print(lst)
