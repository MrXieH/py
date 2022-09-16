# dict
python中的字典，全称dictionary，其他语言中的map，键值对。

```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 增加key
d['Adam'] = 67

# 如果key不存在，dict就会报错，可以通过 in 判断key是否存在
'Thomas' in d # 返回布尔值

# 或者通过get()方法，如果key不存在会返回None或默认值
d.get('Thomas')
d.get('Thomas', 'default value')

# 删除key
d.pop('Bob')
```

和list比较，dict有以下几个特点：
- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。

而list相反：
- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。

dict是用空间来换取时间的一种方法。


# set
和dict类似，也是key的集合，不存储value，key不重复
```python
s = set([1, 1, 2, 2, 3, 3]) # {1, 2, 3}

s.add(4)
s.remove(4)
```
set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等

## 不可变对象
```python
# list为内容可变
a = ['c', 'b', 'a']
a.sort()
# a ['a', 'b', 'c']


# str为不可变，变量a的值最后仍为'abc'
a = 'abc'
a.replace('a', 'A') # 'Abc'
# a 'abc'
```