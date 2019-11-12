"""
编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。

"""
# def make_shirt(size, style):
#     print(f'Your T-shit size is {size},style is {style}')
#
# make_shirt('175', 'hello')
#

"""
需求：进入系统之后显示系统功能界面，功能如下：
1、添加
2、删除
3、修改
4、查询
5、显示
6、退出

步骤：
1、显示功能界面
2、用户输入功能序号
3、按照用户输入的序号，执行不同的功能
"""

"""
# reduce 函数的作用：每次func计算结果继续和下一个元素做累计计算
"""
import functools

list1 = [1, 2, 3, 4, 5]


def func(a, b):
    return a + b


result = functools.reduce(func, list1)

print(result)
