# def fib(n):
#     index = 0
#     a = 0
#     b = 1
    
#     while index < n:
#         yield b
#         a,b = b,a+b
#         index += 1
    
# fib = fib(100)
# print(fib)

# def myfunc(n):
#     return  lambda a:a*n
    
# mydoubler = myfunc(3)
# mytripler = myfunc(4)

# print(mydoubler(11))
# print(mytripler(11))


import ray
import time

# Start Ray.
ray.init()

@ray.remote
def f(x):
    time.sleep(1)
    return x

# Start 4 tasks in parallel.
result_ids = []
for i in range(4):
    result_ids.append(f.remote(i))
    
# Wait for the tasks to complete and retrieve the results.
# With at least 4 cores, this will take 1 second.
start = time.time()
results = ray.get(result_ids)  # [0, 1, 2, 3]
end = time.time()

print(results,end-start)