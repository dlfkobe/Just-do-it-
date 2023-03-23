# f1 = open("./runoob/test.py",'r+',encoding='utf-8')
# f2 = open("./test.py",'w+',encoding='utf-8')
# lines = f1.readlines()
# f2.writelines(lines)

# f1.close()
# f2.close()
# 找所有后缀为是py的所有文件

import os,sys


def find_suffix_with_py_files(dirpath,path_list):
    
    pass

if __name__ == "__main__":
    while True:
        dirpath = input("请输入目录路径：")
        # 如果它是个文件夹
        if os.path.isdir(dirpath)==True:
            break
    path_list = []
    find_suffix_with_py_files(dirpath,path_list)
    print(path_list)
    
    