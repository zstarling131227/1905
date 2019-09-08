# 自定义复合类型
import numpy as np

# data 每一个元组是两个字符，3个数值，一个数值
data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 一个字节占8位。一个字符占2个字节，一个汉子4个字节，32表示32位，也就是4个字节。
# 第一种设置dtype的方式
a = np.array(data, dtype='U2, 3int32, int32')
print(a)
print(a[0]['f0'], ":", a[1]['f1'])
print("=====================================")
# 第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str_', 2),
                          ('scores', 'int32', 3),
                          ('ages', 'int32', 1)])
print(b[0]['name'], ":", b[0]['scores'])
print("=====================================")

# 第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ":", c[0]['scores'], ":", c.itemsize)
print("=====================================")

# 第四种设置dtype的方式
d = np.array(data, dtype={'names': ('U3', 0),  # 0 表示从第0个字节输出。U3表示用3个字符，也就是12个字节。
                          'scores': ('3int32', 16),  # 16表示从第16个字节输出。3int32表示3个整数字字符。
                          'ages': ('int32', 28)})
print(d[0]['names'], d[0]['scores'], d.itemsize)

print("=====================================")

# 第五种设置dtype的方式（仅限于了解）
e = np.array([0x1234, 0x5667],
             dtype=('u2', {'lowc': ('u1', 0),
                           'hignc': ('u1', 1)}))
print('%x' % e[0])
print('%x' % e[1])
print('%x %x' % (e['lowc'][0], e['hignc'][0]))
print('%x %x' % (e['lowc'][1], e['hignc'][1]))

print("=====================================")
# 测试日期类型数组(年月日中间必须为-，时分秒必须为：)
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
f = f.astype('M8[D]')   # 精确到day的datetime64类型
print(f)
print(f[3] - f[0])
f = f.astype('int32')
print(f)
print(f[3] - f[0])

print("=====================================")
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.T)

for x in a.flat:
    print(x.imag)
