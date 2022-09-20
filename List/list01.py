items1 = ['1', '2', 'python']
items2 = [3, 4, 5]

items3 = items1 + items2
print(items3)

print(['hello'] * 3)

items1.append('abc')  # 插在末尾
print(items1)

# items1.remove('python')  # 删除元素
# print(items1)
#
# items1.pop(2)  # 删除指定位置的元素
# print(items1)
#
# items1[1] = 'Python'  # 修改指定位置的元素
# print(items1)

# 查找
print('abc' in items1)  # in 查找

value = items1.index('python')  # index
print(value)

n = items1.count('python')  # 数量
print(n)

# 排序
list1 = [1, 0, 4, 73, 7, 2, 5]
list1.sort()  # 默认升序
print(list1)

list1.sort(reverse=True)  # reverse=Ture:降序       False:降序
print(list1)

# 反转
list1.reverse()
print(list1)


