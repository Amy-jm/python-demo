"""
继承的用法
 子类继承父类，并且可以使用父类的方法和属性
 多重继承，如果父类的属性和方法一模一样，子类继承父类默认继承第一个
"""
'第一个父类'


class C(object):
    def __init__(self):
        self.num = 10

    def info_print(self):
        print(f'{self.num}')


class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(f'{self.num}')


'子类调用父类，第一个父类为C，第二个父类为A'


class B(C, A):
    pass


'实例化一个变量'
resault = B()
'打印变量属性'
print(resault.num)
'变量调用父类方法'
resault.info_print()
print(B.__mro__)
