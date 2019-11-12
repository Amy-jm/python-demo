"""
下标查找数据
"""
name_list = ["Tom","Amy","Rose"]
#
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])
#
# print(name_list.index("Amy", 0, 40))  # 查找
# print(name_list.count("Tom"))  # 统计某个数据出现次数
# print(len(name_list))  # 统计列表数据个数
#
# print("Tom" in name_list)  # 判断数据表在列表
# print("Tom" in name_list)
#
# print("Tom"not in name_list) # 判断数据不在列表
# print("TomS" not in name_list)


# 需求：注册账号判断是否重复

# name = input(f'请输入你要注册的用户名')

# if name in name_list:
#     print(f'用户名已经存在')
# else:
#     print(f'用户名不重复，请继续操作')

# ------------append列表结尾追加序列----------------
#     name_list.append('123')
#     print(name_list)

# 注意：这里是把整个列表都加入进入
# name_list.append(['12','13'])
# print(name_list)
#
# # -----------extend列表结尾追加数据-----------------
# # 注意点：extend追加数据是加列表中的数据
# name_list.extend(['67', '89'])
# print(name_list)

#  -----------insert 插入-------------------
# name_list.insert(2,"zjm")
# print(name_list)

# -----------del 删除列表-----------------------

# del 可以删除指定下标的数据
# # del name_list  # 删除整个列表
# del name_list[0]  # 删除某个
# print(name_list)

# ---------------pop删除-----------------
# 不指定下标，表示删除最后一个




"""
while遍历 依次打印列表中的数据
"""
# i = 0

# while i < len(name_list):
#     print(name_list[i])
#     i +=1

"""
for 遍历
"""

# for i in name_list:
#     print(i)




















