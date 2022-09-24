# 遍历输入的路径中所有文件夹下,所有大小大于1MB,创建时间大于10天的docx文件


import glob
import os
import datetime

path = input('请输入要查询的路径:')
os.chdir(path)

paths = glob.glob('**/*.xlsx', recursive=True)  # 遍历文件夹下的所有文件后缀为.docx的文件

for path in paths:
    file_sizes = os.stat(path).st_size / 1024 / 1024
    file_modify = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
    days = (datetime.datetime.now() - file_modify).days
    if (file_sizes > 1) and (days > 10):
        print(f'压缩包的路径名称是:{path},大小为{file_sizes}MB,创建文件的年份是:{file_modify}'.format(path, file_sizes, file_modify))
