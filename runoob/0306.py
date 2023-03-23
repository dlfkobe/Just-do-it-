# import time
# x = time.strftime('%Y%m%d',time.localtime(time.time()))
# print(x,type(x))
# # x.split("")
# # print(x.remove("-"))
test = ['0','0','0','1','2','3','0','4','5','6','0','0','0','7','8','0','9','0']
# print(test,type(test))
# x.remove x.discard

start = -1
x = range(len(test))
index = 0
for i in test:
    if i!='0' :
        start = index
        break
    index+=1
front = test[0:start+1]
print(front,type(front))
end = test[start+1:]
while end.count('0')>0:
        end.remove('0')
res =  front + end

print(test)
print(res)
    

        
        
    


    
    
        