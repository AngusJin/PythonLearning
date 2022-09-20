# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# import random
#
# center = 10
# count = 0
#
# position = random.randint(1, 10)
# while position != center:
#     print('未命中')
#     position = random.randint(1, 10)
#     count += 1
#
# print('命中', '次数 = %d' % count)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d\t' % (i, j, i * j), end='')
#     print()


# for i in range(0, 20, 2):
#     print(i)

# i = 0
# total = 0
# num = 0
# while i < 5:
#     i += 1
#     total += i
#     # break  终止循环
#     # continue  跳过下方的语句
#
# print(total)


total = 0
for i in range(1, 6):
    total += i
    i += 1
else:
    print(total)

