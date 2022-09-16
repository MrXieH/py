#!/usr/bin/env python3
# 加上shebang可直接执行 calc.py
print(2**10)

import math

def quadratic(a, b, c):
    x1, x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')