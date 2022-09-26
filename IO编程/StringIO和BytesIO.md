# 在内存中读写数据

# StringIO
在内存中写入string
```python
from io import StringIO
f = StringIO() # or f = StringIO('hi!')
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) # hello world!
```

# BytesIO
在内存中写入二进制数据
```python
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) # 写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'
```