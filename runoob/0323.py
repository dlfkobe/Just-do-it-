
# # import time
# # # nowTime = datetime.datetime.now() + datetime.timedelta(days=days)s
# # # clock = "09"
# # # specified_time = time.strftime("%Y-%m-%d",time.localtime()) + " {}:00:00".format(clock)
# # # timeArray = time.strptime(specified_time, "%Y-%m-%d %H:%M:%S")
# # # begin = int(time.mktime(timeArray))
# # # end = int(time.time())
# # # print(begin,end)

# # test1 = int(time.time())
# # # print(test)
# # time.sleep(13)
# # test2= int(time.time())
# # print(test2-test1)

# # Timestamp of the specified time
# # def get_timestamp_spec_time(clock, days=0):
# #     """
# #     获取指定的时间点的时间戳
# #     @param clock: 钟点;指定的时间,比如当天的凌晨一点,钟点即为1(24小时制)
# #     @param days:  与当前时间的相差的日期。-1 表示昨天；0 表示当天(默认)；1 表示明天
# #     @return:      返回时间戳
# #     """
# #     nowTime = datetime.datetime.now() + datetime.timedelta(days=days)
# #     specified_time = nowTime.strftime("%Y-%m-%d") + " {}:00:00".format(clock)
# #     timeArray = time.strptime(specified_time, "%Y-%m-%d %H:%M:%S")
# #     return time.mktime(timeArray)

# # 文件夹操作 一般注意可能要递归，因为文件夹下还有文件夹

# def file_repalce(file_name,rep_word,new_word):
#     with open(file_name,'r+',encoding='utf-8') as f_read:
#         content = []
#         count = 0
        
#         for line in f_read.readlines():
#             if rep_word in line:
#                 count = count + line.count(rep_word)
#                 new_line = line.replace(rep_word, new_word)
#             content.append(new_line)
        
#         decide = input("\n文件 {} 共有 {} 个 {}, 您确定要全部替换吗? \n【YES/NO】".format())
         
#         if decide.upper() == 'YES':
#             with open(file_name,'w+',encoding='utf-8') as f_write :
#                 f_write.writelines(content)
            
        
        
# if __name__ == '__main__':
#     file_repalce("./runoob/test.txt",'s','qwe')
            

import os
# print(os.getcwd())
# path = r"C:/Users/User/Desktop/study"
# os.chdir(path)
# 
# print(os.getenv())
# print(os.getcwd())  # 当前目录
# print(os.pardir)
# x = os.path.join(os.getcwd(),os.pardir)
# y = os.getcwd()
# print(x)
# print(os.path.abspath(x))
# print(os.path.abspath(y))

# file_name = __file__
# print(file_name,end="\n\n")
# file_abs = os.path.abspath(file_name)
# print(file_abs,end="\n\n")
# print(os.path.dirname(file_name),end="\n\n")


file_name = __file__
# print(os.path.basename(file_name))
# print(os.path.getsize(file_name))
fake_file = os.path.join(os.path.dirname(file_name),"test.py")

# print(fake_file)
# dir_name = os.path.dirname(file_name)
# print(os.path.isdir(fake_file))
# print(os.path.isdir(dir_name))
# print(os.path.split(file_name))
# print(os.path.splitdrive(file_name))
# print(os.path.exists(fake_file)
# print(file_name)
# print(os.path.splitext(file_name))
# print(os.path.dirname(file_name))
