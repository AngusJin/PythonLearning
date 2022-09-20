import random


# def generate_random(n=5):
#     ran_list = []
#     for i in range(n):
#         ran = random.randint(1, 10)
#         if ran == 6:
#             return ran
#         ran_list.append(ran)
#
#     print(ran_list)
#
#
# r = generate_random(n=10)
# print(r)


def get_lisit_total(n=5):
    total = 0
    ran_list = []
    for i in range(n):
        ran = random.randint(1, 50)
        ran_list.append(ran)
        total += ran
    return total, ran_list


result = get_lisit_total(5)

print(result)
