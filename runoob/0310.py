# 迭代器 生成器

# def my_gene_func():
#     index = 0
#     test = [1,2,3,4]
#     yield test[index]
#     index += 1
    
# gene = my_gene_func()
# print(next(gene))
# print(next(gene))
# print(next(gene))
# print(next(gene))

def mytask1():
    print('task1 开始执行')
    # print(i)
    yield
    print("继续1")
    return
    
def mytask2():
    print('task2 开始执行')
    # print(i)
    yield
    print("继续2")
    
    
gene1 = mytask1()
gene2 = mytask2()

for i in range(10):
    next(gene1)
    next(gene2)
