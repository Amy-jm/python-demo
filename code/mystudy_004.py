"""
切片：语法 序列码[起始下标：结束下标：步长]

序列号的特点左闭右开

步长不写默认1

起始结束、步长都可以正数或者负数

"""
# str = "0123456789"
# # print(str[0:3])
# # print(str[0:3:2])
# # print(str[:5])  # 开始不写默认从0开始
# # print(str[2:])  # 结束不写默认到结尾
# # print(str[:])  # 开始和结束都不写默认从开始到结束
# # print(str[::-1])  # 步长为负数，表示倒序选取
# # print(str[-4:-1])  # 倒序选取下标-1表示最后一个数字，注意序列号的特点左闭右开
# print(str[-4:-1:-1])  # 如果选取方向和步长选取方向不一致，选取内容为空


"""
字符串查找
find方法
index方法
count方法
"""

str1 = "hello ,me name is zjm,he name is Tom."

print(str1.find('is'))  # 找到第一个is的位置
print(str1.count("is"))  #在整个字符串中找到2个is 字符
print(str1.index("is"))  # 找到第一个is的位置
print(str1.find("is",20,50))  # 在20-50字符中查找is的位置
print(str1.count("is",20,50))  # 在20-50字符中查找is的位置
print(str1.index("is",20,50))  # 在20-50字符中查找is的位置
print(str1.find("and"))  # 没有找到这个字符为-1
print(str1.count("and"))  # 统计字符为0个
# print(str1.index("and"))  # 没有这个字符子串报错

# rfind、rindex 从右边开始查找

print(str1.rfind("is"))  # 从右边开始查找
print(str1.rindex("is"))

# 修改replease(替换)、split()分割、join（拼接）
# ------------替换---------------
print(str1.replace("is","how"))  # 不填写默认次数全部替换
print(str1.replace("is","how",1))  # 只替换一个how
# ------------分割---------------
print(str1.split("is"))  # 分割返回一个列表，分割字符串丢失
# ------------拼接---------------
str2 = ["aa", "bb", "cc"]
new_str2 = "...".join(str2)
print(new_str2)


print(str1.capitalize())  # 字符串首字母大写
print(str1.title())  # 字符串每个单词首字母都大写
print(str1.upper())  # 小写转大写
print(str1.lower())  # 所有变小写


str3 = " hello ,my name is zjm    "
print(str3.lstrip())  # 删除左侧空白
print(str3.rstrip())  # 删除右侧空白
print(str3.strip())  # 删除两侧空白

print(str1.startswith("He"))  # 判断是否为He开头
print(str1.startswith("he"))  # 判断是否为He开头

print(str1.endswith("TOM"))  # 判断是否以TOM为结尾
