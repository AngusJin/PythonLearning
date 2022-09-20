import detective


def service():
    print('为人民服务')


print(detective.name)
detective.detect('xxx')

c = detective.Course('柯南', [])
# c.add_course('语文')

print(c.c_list)

# c.remove_course('数学')
# c.remove_course('语文')
# c.remove_course('英语')
# c.remove_course('英语')
# print(c.c_list)
