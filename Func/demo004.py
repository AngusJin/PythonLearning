class Phone:
    # 属性
    # brand = '品牌'
    # color = '黑色'
    # price = '10000'

    def __init__(self, brand, price):
        print('__init')
        self.brand = brand
        self.price = price

    # 方法
    def call(self):
        print('%s手机使用call方法' % self.brand)

    def send_message(self):
        print('sendMessage方法')


# p1 = Phone()
# p1.brand = '品牌1'
# print(p1.brand)
# p1.call()
# print('-------------')
# p2 = Phone()
# p2.send_message()
# print(p2.price)


p1 = Phone('品牌', '4k')
p1.call()
