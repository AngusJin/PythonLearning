# import sys
#
# print(sys.path)  # 结果为列表
#
# for p in sys.path:
#     print(p)


import os

os.chdir('/Users/jinhandong/PycharmProjects/Learn')

print(os.getcwd())

dir_list = os.listdir()
print(dir_list)

