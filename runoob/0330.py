# import os,shutil
# # print(os.getcwd())
# # print(os.getenv())
# # print(dir(os))
# # print(help(os))
# import glob
# print(glob.glob("../Just-do-it-/*.py"))

# import sys
# print(sys.argv)
# import smtplib

# server = smtplib.SMTP('localhost')
# server.sendmail('1903152827@qq.com', '1756737900@qq.com',
#  """To: 1903152827@qq.com
#  From: 1756737900@qq.com

#  Beware the Ides of March.
#  """)
# server.quit()

# from datetime import date

# day = date(2022,10,23)
# days = date.today()- day
# print(days)


# def average(values):
#     """Computes the arithmetic mean of a list of numbers.

#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

# import doctest
# print(doctest.testmod()  )   # 自动验证嵌入测试


import datetime
import time
# 今天
# print(datetime.time())
# print(time.time())
# today = datetime.date.today()

# # yesterday = datetime.date(2023,3,1)
# # print(yesterday-datetime.timedelta(days=1))

# # print(datetime.date.today())

# # print(today.month)
# last_month = today.month - 1 if today.month - 1 else 12
# print(last_month)

# 时间戳转 datetime
# print(datetime.datetime.fromtimestamp(time.time()))
# dattimestamp = time.mktime(datetime.date.today().timetuple())
# print(datetime.datetime.fromtimestamp(dattimestamp))

import math ,random
# print(math.trunc(123))
# print(random.randrange(3))

# print(0.1 + 0.2 == 0.3)

x = "ashdk"
y = "as"

# print(x.__contains__(y)
# )

import operator
print(
operator.eq(x,y)

)