import random


def login():
    username = input('用户名：')
    password = input('密码：')

    if username == '123456' and password == '123456':
        print('输入正确')
    else:
        print('输入错误')


print(login)
login()


def generate_random():
    for i in range(5):
        ran = random.randint(1, 10)
        print(ran)


generate_random()
