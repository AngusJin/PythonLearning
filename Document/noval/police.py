# import detective

import detective as dtt  # import...as... 引入并重命名


def service():
    print('为人民服务')


print(dtt.name)
dtt.detect('xxx')

c = dtt.Course('柯南', ['xxx'])
# c.add_course('语文')

print(c.c_list)

# c.remove_course('数学')
# c.remove_course('语文')
# c.remove_course('英语')
# c.remove_course('英语')
# print(c.c_list)



