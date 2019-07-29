######作业4
"""
4. 已知：加速度，初速度，时间
　　计算：距离
　　加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方
"""
initial_velocity = int(input("初速度是（米每秒）："))
time = int(input("时间是（秒）："))
accelerated_speed = int(input("加速度是（米每平方秒）："))
distance = initial_velocity * time + 0.5 * accelerated_speed * time ** 2
print("位移是：" + str(distance) + "m")
######作业5
"""
5. 温度
　　摄氏度 = (华氏度 - 32) / 1.8
　　华氏度 = 摄氏度 * 1.8  + 32
   开氏度＝ 摄氏度　＋　273.15
   (1)在控制台中获取华氏度，计算摄氏度。
   (1)在控制台中获取，计算华氏度。
   (1)在控制台中获取摄氏度，计算开氏度。
"""
fahrenheit_degree = float(input("请输入温度："))
degree_centigrade = (fahrenheit_degree - 32) / 1.8
print(degree_centigrade)
degree_centigrade = float(input("请输入温度："))
fahrenheit_degree = degree_centigrade * 1.8 + 32
print(fahrenheit_degree)
degree_centigrade = float(input("请输入温度："))
degree_kelvin = degree_centigrade + 273.15
print(degree_kelvin)
######作业7
"""
7.（扩展）在控制台中获取总秒数，计算几小时零几分钟零几秒。
"""
number = int(input("请输入秒数:"))
hour = number // 3600
minute = number % 3600 // 60
second = number % 3600 % 60 % 60
print(hour,"小时",minute,"分",second,"秒")
