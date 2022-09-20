import random


def generate_random(n, a, b):
    for i in range(n):
        ran = random.randint(a, b)
        print(ran, end=' ')
        if ran == 66:
            print('\n次数为:%d' % i)
            break


generate_random(99, 1, 100)
