"""
1.书写input
input（'提示信息'）
2.观察input特点
  遇到input，等待用户输入
  接到input存变量
  input接收到的数据类型都是字符串
"""

password = input('请输入密码：')
print(f'您输入的密码是{password}')
print(type(password))

print(type(int(password)))
print(int(password))
print(type(float(password)))
print(float(password))
print(type(str(password)))
print(str(password))
