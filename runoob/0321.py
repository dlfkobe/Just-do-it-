# res = {

# }
# datalist = []
# res["a"] = datalist
# print(res)
# datalist = [1,2,3]
# print(res)

# X = 10^6
# print(X)

# repr() 展示数据类型信息，适合开发与调试阶段

# f = open('./test.txt','a+',encoding='utf-8')
# print(f.tell())
# f.seek(0)
# text = f.readlines()
# print(text)

test = "2023-03-15 09:00:00"
x = test.split("-")
day = (x[-1].split(" "))[0]
print(x)
print(day)
prefix = x[0]+x[1]+day
print(prefix,type(prefix))