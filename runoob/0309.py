# test = [1,2,3,4]
# it = iter(test)
# # print(next(it))
# for x in it:
#     print(x)

# import sys
# test = [1,2,3,4]
# it = iter(test)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
        
# 迭代器  
# class MyNumbers:
#     def __iter__(self):
#         self.num = 0
#         return self
#     def __next__(self):
#         if self.num <=100:
#             x = self.num
#             self.num += 2
#             return x
#         else:
#             raise StopIteration
        
# test = MyNumbers()
# myiter = iter(test)

# for x in myiter:
#     print(x)

# 生成器
import sys

def fibonacci(n): # 使用了yield的函数被称为生成器 generator
    a,b,counter = 0,1,0
    while True:
        if counter > n:
            return
        yield b
        a,b = b,a+b
        counter += 1
    
f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
    

        
        