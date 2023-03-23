import json
a = [1,2,[3,[4,5]]]
# print(str(a))
x = eval(str(a))
a[-1][-1] = 1000


print(x,type(a))