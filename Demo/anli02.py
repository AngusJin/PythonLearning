# import os
#
# for dirpath, dirnames, files in os.walk('./'):
#     print(dirpath, dirnames, files)


import glob

t_list = glob.glob('**')  # 获取当前目录下的文件夹和文件
# t_list = glob.glob('**/') # 获取当前目录下的文件夹
# t_list = glob.glob('**/', recursive=True) # 可以遍历出所有子目录的文件夹
# t_list = glob.glob('**/*.py', recursive=True) # 可以遍历出所有子目录的文件夹中的.py文件
print(t_list)


