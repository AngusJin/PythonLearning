s = 'abcdefghij'
#    0123456789
print(s[5])  # 字符串中下标为5的字符
print(s[-2])  # 倒数第二个字符


# 切片 字符串名字[start:end:step]    包含左边不包含右边
print(s[0:4])
print(s[5:])
print(s[:5])
print(s[0:9:3])  # 不包含[9]
print('---------')
print(s[:6:-1])
print(s[6:-1])
