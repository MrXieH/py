import random

# 生成随机字符串
def generator_random(count, length):
    # count 生成数量
    # length 字符串长度
    s = 'abcdefghijklmnopqrstubwxyz1234567890~!@#$%^&*'
    result = []
    for x in range(count):
        result.append(''.join(random.sample(s, length)))
    return result


if __name__ == '__main__':
    print(generator_random(200, 10))
