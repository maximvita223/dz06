# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
# n = int(input())
# kit_num = []
# sum_num = 0
# count = 1
# for i in range(n):
#     kit_num.append((1+1/count)**count)
#     sum_num += kit_num[i]
#     count += 1
# print(kit_num)
# print(sum_num)

n = int(input("Введите число: "))
kit = [(1+1/i)**i for i in range(1, n+1)]
print(sum(kit))

print(kit)
