# import keyword

# print(keyword.kwlist)
# test = '''
# sdahjk    sedf      
# dashdndsf   
# adsl  sdf
# '''
# # print(test)
# import sys
# for i in sys.argv:
#     print(i)
# print("python 路径为",sys.path)

# import sys
# print(sys.path)    
# import sys
# 张三 = '25.67'
# print(int(张三))

# a = b = c = 1
# a = 2
# b = 3
# print(id(a),id(b),id(c))
# print(a,b,c)


# test = "123456789"
# print(test[0:])
# # print(test[0:-1:-1])
# print(test[::-1])

# from ast import literal_eval
# def reverseWords(words):
#     inputWords = words.split(' ')
#     inputWords = inputWords[::-1] # [-1::-1]
#     print(inputWords)
    
#     output = ' '.join(inputWords)
#     return output

# if __name__ == '__main__':
#     words= "sjhd asjiuhd df"
#     print(reverseWords(words))

# import sys
# print(sys.path)
# a = {1,2,3}
# b = {2,5,6}
# print(a^b)
# # x ="[{'key':1,'symbols':[1,2,3]},{'key':2,'symbols':[1,2,3]},{'key':3,'symbols':[1,2,3]}]"
# # a = literal_eval(x)
# # print(a,type(a))

# dict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
# # print(dict.keys())
# for key in dict.keys():
#     print(key)

# a = {"str"+str(x) : x**2 for x in (2,3,4)}
# print(a)
# a.clear()
# print(a)

# s = "suhdkas\nsadhg\tsad"
# print(s)
# print(repr(s))
# x = dict(a='sadf',b="shdli")
# print(x)

# a = dict(x=5,y=0)
# print(a)

# keyList = [1,2,3,4]
# valueList = ["a","b","c","d"]
# a = dict(zip(keyList,valueList))
# print(a)

# a = {1,2}
# b = frozenset(range(5))
# c = set(range(5))
# a.add(b)
# a.add(c)
# print(a)
# print(b)

# x = chr(65)
# print(x)
# y = ord(x)
# print(y)
# x = 1289743
# print(hex(x))
# print(oct(x))

# def test(*args):
#     print(args)

# test(1,23,23,"shj")

# dict1 = {"key"+str(x) : x**2 for x in range(5)}
# print(dict1)
# for k,v in dict1.items():
#     print(k,v)
# x = ['A','B','C','D']
# y = ['a','b','c','d']

# a = dict(zip(x,y))
# print(a)

# '''推导式'''
# res = [ x for x in range(30) if x % 3 == 0 ]
# print(res)

# listDemo = ['Google','Runoob','Taobao']
# newDcit = { key : len(key) for key in listDemo}
# print(newDcit)

# a = (x for x in range(1,10))
# print(a)

# list1 = ['python','java','go','ruby']
# # list2 = [ x.title() if x.startswith('p') else x.upper()  for x  in list1  ]
# # print(list2)

# a = 10
# b = 10
# print(a==b)
# print(id(a)==id(b))

# # n := len(list1)
# # -*- coding: utf-8 -*-


# x =['1','2','3','4','5','6','7','8','9']
# x = [ int(t) for t in x ]
# print(x)

# -*- coding: utf-8 -*-

# class Solution:
#     def NumberOf1(self,n):
#         if n>=0:
#             return bin(n).count('1')
#         else:
#             return bin(2**32 + n).count('1')
    
# if __name__ == '__main__':
#     solution = Solution()
#     solution.NumberOf1


# a = 17
# x = bin(a)
# print(x,type(x))

# def NummerOf1(n):
#     cnt = 0
#     if n < 0 :
#         n = n & 0xffffffff
#     while n :    
#         cnt += 1
#         n = (n - 1) & n
#     return cnt

# count = 0
# a = 15
# while a:
#     if a & 1 == 1:
#         count+=1
#     a >>= 1
    
# print(count)
    

# x = 17
# print(NummerOf1(x))
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           