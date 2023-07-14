s = 'Pythonxxxabcdefgh'

print(s.find('abc'))  # 从左开始找
print(s.rfind('fgh'))  # 从右开始找
print(s.find('sss'))  # -1 未找到

try:
    s1 = 'abca'
    print(s.index(s1))
except:
    print("%s不存在" % s1)


s2 = 'xxx'
print(s.index(s2))


'''
    try:
    catch:
'''
'''
    find找不到返回-1
    index找不到报错
'''

# replace
print(s.replace('xxx', '哈哈哈'))

print(s)

print(s.startswith('xxx'))
print(s.endswith('h'))

print(s.isdigit())  # 是否为数字
print(s.isalpha())  # 是否为字母
