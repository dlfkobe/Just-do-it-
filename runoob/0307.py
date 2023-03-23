# set.discard()
# set.remove()  # 删除不存在的元素会报错
# 交集 intersection
# 差集  difference
# 并集 union
# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
# z = x.symmetric_difference(y)
# print(z)

# x = {}  false
# if x:
#     print("true")
# else:
#     print("false")

# myStatus = 400
# def http_error(status):
#     match status:
#         case 400:
#             print("Bad Request")
#         case 404:
#             print("Not Found")
#         case 418:
#             print("I'm a teapot")
#         case 500:
#             print("Internal Server Error")
#         case _:
#             print("error")

# fibonacci series：
# a,b = 0,1
# while b<10:
#     print(b)
#     a,b = b,a+b

# print(1,2,3,sep=",")

# def fabonacciSeries(num):
#     if num<1:
#         print("输入有误")
#         return -1
#     elif num==1 or num==2:
#         return 1
#     else:
#         return fabonacciSeries(num-1)+fabonacciSeries(num-2)


# test = [1,2,3,4,5,[2,[3,4]]]
# import copy
# x= copy.deepcopy(test)
# test[-1][-1]=1280
# print(x,test,sep="     ")

# 迭代器 生成器
test = [1,2,2,3,4,5,6,7]
it = iter(test)
for x in it:
    if x==2:
        test.remove(x)
print(test)