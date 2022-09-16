# list
list是一种有序的集合

```python
classmates = ['Michael', 'Bob', 'Tracy']
# 可以不同类型
classmates = ['Apple', 123, True, ['asp', 'php']]

# len函数获取长度
len(classmates) # 3

# 使用索引访问 超出索引会报错，最后一个索引为 len(classmates) - 1
classmates[0] # Michael
classmates[-1] # Tracy 倒数第一个

# 追加末尾
classmates.append()

# 插入到指定的位置
classmates.insert(1, 'Jack')

# 删除末尾
classmates.pop()  # 返回被删除项

# 删除指定
classmates.pop(1)

# 修改元素
classmates[1] = 'Sarah'
```

# tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
```python
classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的

# 注意，定义tuple的陷阱
t = (1, 2) # 正常定义
t = () # 定义一个空的tuple

# 如果定义一个只有一个元素的tuple
t = (1) # 这样是错误的，因为()括号可以表示tuple，也可以表示数学中的括号，所以这样被理解为数字1
t = (1,) # 这样是正确的，需要使用,来消除歧义
```
tuple中包含的应用类型内容是可变的，如包含list

```python
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
```
