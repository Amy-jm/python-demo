"""
需求：
  如果年龄小于18，为童工，不合法；
  如果年龄为18-60之间，为合法工作年龄；
  如果年龄大于60为退休年龄；
"""

# age =int(input(f'请输入您的年龄：'))
#
# if age < 18:
#     print(f'如果年龄小于18，为童工，不合法；')
# elif 18 >= age <=60:
#     print(f'如果年龄为18-60之间，为合法工作年龄；')
# else:
#     print(f'如果年龄大于60为退休年龄；')
#
"""
需求：坐公交车
如果有钱可以上车
如果没有钱不能上上车
如果有钱且有作为可以坐下
如果有钱无座位，只能站着
"""
#
# money = float(input(f'您投入的金额:'))
# if money > 0:
#     seat = int(input(f'公交车上是否有座位'))
#     if seat >=1:
#         print(f'有座位')
#     else:
#         print(f'没有座位')
# else:
#     print(f'无法乘坐公交车')
"""
需求：重复打印某句话
"""
# i = 0
# while i < 5:
#     print(f'hello')
#     i += 1
# print(f'hello,yes')

"""
需求：计算1-100中偶数相加
1.数据为0-100使用循环取出
2.和2取余为0 为偶数
3.把去除的偶数相加

"""
# i = 0
# s = 0
# while i < 101:
#     if i % 2 == 0:
#         s += i
#     i += 1
# print(s)

"""
需求：计算1-100中偶数相加
初始为0 ，每次递增2，为偶数
"""
# i = 0
# # s = 0
# #
# # while i < 101:
# #     s += i
# #     i += 2
# # print(s)

"""
打印99乘法表
"""
# j = 1
# while j <= 9:
#     i = 1
#     while j >= i:
#         s = i * j
#         print(f' {i} * {j} = {s}', end="\t")
#         i += 1
#     print(end="\n")
#     j += 1


# """
# for循环语法
# """
# i = 0
# str1 = "hello"
# for i in str1:
#     print(i)




