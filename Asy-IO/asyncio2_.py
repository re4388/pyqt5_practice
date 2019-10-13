import asyncio
import threading



@asyncio.coroutine
def hello():
    print(f'Hello world { threading.currentThread()}')

    # 把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行
    yield from asyncio.sleep(2)
    
    print(f'Hello again { threading.currentThread()}')



# create/subcalss a loop obj
loop = asyncio.get_event_loop()

# 用Task封装两个coroutine 
tasks = [hello(), hello()]

# exec the coroutine
loop.run_until_complete(asyncio.wait(tasks))

# close it
loop.close()
