# Дан список чисел напишите программу создающюю список из нечетных чисел

# lst = [1,2,3,4,5,10]
# lst1 = []
# for i in lst:
#     if i%2!=0:
#         lst1.append(i)
# print(lst1)

lst = [1, 2, 3, 4, 5, 10]
lst = list(filter(lambda x: x % 2 != 0, lst))
print(lst)
