#!/usr/bin/python3

# import time
# ticks = time.time()
# print("当前时间戳为",ticks)
import time
# localtime = time.localtime(time.time())
# print("本地时间为",localtime)
# localtime = time.asctime(time.localtime(time.time()))
# print(time.localtime())
# start = "2023-01-01 00:00:00"
# # strftime strptime
# # print(time.mktime(time))
# start_time = time.mktime(time.strptime(start, "%Y-%m-%d %H:%M:%S"))
# now = time.time()
# day_in_year = (now - start_time)/24/60/60
# print(day_in_year)

# zone = time.strftime("%Z %y-%m-%d %H:%M:%S",time.localtime())
# print(zone)



# import calendar
# cal = calendar.month(2023,3)
# print(cal)
# import time
# start = time.process_time()
# for i in range(10000):
#     i = i**10
# end = time.process_time()
# print(end - start)

# '''
# time 总结

# time.
# '''
# print(time.timezone())
# print(time.gmtime(time.time()))  相当于 time.localtime()
# print(time.localtime())

# 数据结构
# test = [1,2,3,4,6,5]
# # test = test.sort().reverse()
# test = test.sort(reverse= True)
# # test.reverse()
# print(test)

# 列表当作堆栈用
# 队列 使用deque
# from collections import deque
# queue = deque(["asdh","sdhiu","askjdh"])
# queue.popleft()
# print(queue)

# vec = [2,3,4]
# test = [3*x for x in vec]
# print(test)

# test = [str(round(355/113,i)) for i in range(1,6)]                                                                                                                                                                                                                                                                                                                                                                                                                     
# print(test)

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# matrix_T = [[row[i] for row in matrix] for i in range(4)]
# print(matrix_T)

# test = [1,2,3,4,6,5,7,8,9,10,-1,0]
# res = sorted(test)
# print(res)

# dict 可以直接传入元组列表，进行构造
# 推导式

# test = {'gallahad':'the pure','robin':'the brave'}
# for k,v in test.items():
#     print(k,v,sep=" : ")

# test = ["a","b","c","d","e","f","g","h"]
# for i,v in enumerate(test):
#     print(i,v,sep="->")
# import sys
# test = [1,2,3,4,5,6,7,8,9,10]
# test = reversed(test)
# 

# while True:
#     try:
#         print(next(test))
#     except StopIteration:
#         sys.exit()
        
# questions = ['name','quest','favorite']
# answers = ['dlf','nope','study']
# for q,a in zip(questions,answers):
#     print("what is your {0} ? It is {1}".format(q,a))

# test = 1


# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# matrix_T = [[row[i] for row in matrix] for i in range(4)]
# print(matrix_T)

# res = []
# for i in range(4):
#     res.append([])
#     for row in matrix:
#         res[i].append(row[i])
# print(res)

# matrix_T = [[row[i] for row in matrix] for i in range(4)]
# print(matrix_T)

# python 返回多个值其实是元组的装包与拆包

# import sys
# print("命令行参数如下：")
# for i in sys.argv:
#     print(i)
# print("Python 路径为： ",sys.path,'\n')



# # print(globals())
# # print("-----")
# # print(locals())


# # 输入输出

# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
#     print(repr(x*x*x).rjust(4))
    
    
# f = open('./test.py', 'r+',encoding='utf-8')
# print(f.tell())
# f.close()
# res = f.readlines()
# print(res)
# f.close()

# with open('./test.py', 'r+',encoding='utf-8') as f:
#     res = f.read()
# print(res)


# import pickle,pprint

# data1 = {
#     'a':[1,2,3,4.5],
#     'b':('string',u'asdhkj'),
#     'c':None
# }

# data2 = [1, 2, 3]

# with open('./data.pkl','wb') as f:
#     pickle.dump(data1,f)

# with open('./test.py', 'rb') as f:
#     f.seek(0)
#     data1 = pickle.load(f)
# pprint.pprint(data1)

from urllib import request

response = request.urlopen("http://www.baidu.com/")
with open("./mrg.html",'w',encoding='utf-8') as f:
    f.write(str(response.read()))

    