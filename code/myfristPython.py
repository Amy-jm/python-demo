print("Hello,World")

message1 = " Hello World"
print(message1)


message2 = "I'm zjm,"
print(message2 + message1)

# 单行注释







a = 13
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(b**a)
print("my favial number is " + str(a))

c = True
print(type(c))
print(type(a))


"""
1.准备数据
2.格式化输出数据
"""
#1.我今年年龄是X岁
age = 18
name = 'zjm'
weight = 45
stu_id1 = 1

# ff今年X岁
print('ff年%d岁'% age )

# 我的名字是XXX
print('我的名字是%s' %name)

# 我的体重是
print('我的体重是%.2f' %weight)
# %03d，3表示整数位补齐位数，不足往前补齐0，超过位数原样输出数字
stu_id1 = 1
stu_id2 = 1002356
print('我的学号是%03d' % stu_id1)
print('我的学号是%03d' % stu_id2)

# 我的名字是zjm，我今年18岁，体重45公斤，学号是001
print('我的名字是%s，我今年%d岁，体重%.2f公斤，学号是%03d' %(name, age, weight, stu_id1))
print('我的名字是%s，我今年%s岁，体重%s公斤，学号是%s' %(name, age, weight, stu_id1))
print(f'我的名字是{name}，我今年{age}岁，体重{weight}公斤，学号是{stu_id1}')
print(f'我的名字是{name}，\n我今年{age}岁,\n\t体重{weight}公斤,\n学号是{stu_id1}\n')


print(f'我的名字是{name}，我今年{age}岁，体重{weight}公斤，学号是{stu_id1}',end="\n")
print(f'我的名字是{name}，我今年{age}岁，体重{weight}公斤，学号是{stu_id1}',end="...")
print(f'我的名字是{name}，我今年{age}岁，体重{weight}公斤，学号是{stu_id1}',end="...")







