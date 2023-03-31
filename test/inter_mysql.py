import pymysql
import generator_random

# TODO 异常处理

def inter_mysql(couponList = []):
    connect = pymysql.connect(host='42.192.181.203', user='root', password='123456', database='py')
    cursor = connect.cursor()
    inter_sql = 'insert into coupon (id, value) values (%s, %s)'
    for value in couponList:
        cursor.execute(inter_sql, (value, value))
    connect.commit()

inter_mysql(generator_random.generator_random(200, 10))