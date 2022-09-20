# 字典 dict
person = {'姓名': '小明', '年龄': '10', '职业': '学生'}
print(person)
print(type(person))

# 增加
person['性别'] = '男'
print(person)

# 修改
person['年龄'] = '20'
print(person)

# 删除
# person.pop('性别')
# print(person)

del person['性别']
print(person)

# 获取数据
# value = person['姓名']
# print(value)

value = person.get('姓名1', '小红')  # value = person.get('姓名','小红')  没有则返回默认值
print(value)

print('--------')

# 遍历
# for i in person:
#     print(i)
#
# for k in person.keys():
#     print(k)

for j in person.values():
    print(j)

print('--------')

for a, b in person.items():
    print(a,b)
