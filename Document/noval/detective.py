# 变量
name = '柯南'
age = 10


# 函数
def detect(case=None):
    if case:
        print('这个案件:' + case + ',真相只有一个!')
    else:
        print('没有案件')


# 类:课程表
class Course:
    def __init__(self, name, c_list):
        self.name = name  # 学员名
        self.c_list = c_list  # 课程列表

    # 选修课
    def add_course(self, c_name):
        if c_name:
            self.c_list.append(c_name)
        else:
            print('选修课不能为空')

    # 取消选修课
    def remove_course(self, c_name):
        if c_name:
            self.c_list.remove(c_name)
        else:
            print('选修课不能为空')


print(__name__)  # __main__
