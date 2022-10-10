SQLAlchemy 是 python中最有名的ORM(Object-Relational Mapping 对象关系映射)框架,把关系数据库的表结构映射到对象上。

```python
# 假设user表有id和name
[
    ('1', 'xiaoming'),
    ('2', 'xiaohong')
]

# 使用class实例来表示
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'xiaoming'),
    User('2', 'xiaohong')
]
```

```python
$ pip install sqlalchemy

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接: '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：
class School(Base):
    __tablename__ = 'school'
    id = ...
    name = ...
```

由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
```python
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
```

有了ORM，查询出来的可以不再是tuple，而是User对象 SQLAlchemy提供查询接口如下：
```python
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
```

ORM框架也对象之间关联，例如User拥有多个Book
```python
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
```