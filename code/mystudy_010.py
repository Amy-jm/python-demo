"""
需求：洗衣机功能：能洗衣服
    1.定义洗衣机类
        语法：class 类名（）：
            书写代码
    2.创建对象

验证成果
"""


class Washer(object):  # 类
    def __init__(self, width, higth):
        self.width = width
        self.higth = higth

    def wash(self):  # 方法
        print('能洗衣服')
        print(f'higth 的属性是{self.width}')  # 对象内使用属性
        print(f'wigth 的属性是{self.higth}')


# 用类实例化对象
haier = Washer(10, 20)
haier1 = Washer(39, 94)

# 对象调用方法
haier.wash()
haier1.wash()

