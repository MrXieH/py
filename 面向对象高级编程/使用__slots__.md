```python
class Student(object):
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性

from types import MethodType

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

s.set_age = MehotdType(set_age, s) # 使用MethodType动态给实例绑定方法

s2 = Student()
s2.set_age # 没有这个方法，只对s实例有效

# 可以给class绑定，就所有实例都可以用
Student.set_age = set_age
```

# 使用__slots__可以限制实例的属性
```python
# __slots__仅对当前类生效，对实例不生效 
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
s.score = 99 # 绑定属性'score' 绑定失败，报错
```