print(666)
print("黑马程序员")
print(123445)

#定义一个变量
money =50
print("钱包还有：",money)


# 列表类型 list数据变量
list = ['a','b','c','d','e']
print(list[-4:-1])#不包含第-1个元素

# Tuple 元组数据变量
# list和tuple的区别
# 元组元素不能更改，元组的元素写在()
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2 )
print(tuple)
print(tuple[0]+list[0])



# Set 集合
# Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# Dictionary 字典
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
#
# 键(key)必须使用不可变类型。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值


# 条件语句的两种使用
#if...else
num = int(input("输入一个数字："))
if num%2 == 0:
    if num%3 == 0:
        print("你输入的数字可以被2或3整除")
    else :
        print("你输入的数字能被2整除。但不能被3整除")
else :
    print("你输入的数字不能被2或3整除")

# match...case 第二种条件语句的使用


#循环语句的使用

#while
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")