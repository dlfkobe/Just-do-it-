# tinydict = {"name":"sdg","age":23}
# for key,value in tinydict.items():
#     print(key,value)
    
# tinydict.setdefault("name","qwe")
# tinydict.setdefault("sex","male")
# print(tinydict)
 
tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Sex': 'female' }

tinydict.update(tinydict2)
print ("更新字典 tinydict : ", tinydict)
