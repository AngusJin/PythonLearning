import os

path = input('请输入一个路径:')

os.chdir(path)

file_list = []
dir_list = []

for file in os.scandir():
    if file.is_dir():
        dir_list.append(file.name)
    else:
        file_list.append(file.name)

print(f'文件夹的数量是:{len(dir_list)},文件夹是:{dir_list}')
print(f'文件的数量是:{len(file_list)},文件是:{file_list}')

demo_list = []

for name in file_list:
    if 'demo' in name.lower():
        demo_list.append(name)

print(f'demo文件的数量是:{len(demo_list)},文件是:{demo_list}')
