import asyncio
async def func1():
    print("func1开始执行！")
    await asyncio.sleep(6)
    print("func1执行结束")
async def func2():
    print("func2开始执行")
    await asyncio.sleep(2)
    print("func2执行结束")
task1 = asyncio.create_task(func1())
task2 = asyncio.create_task(func2())
asyncio.run(task1)
asyncio.run(task2)