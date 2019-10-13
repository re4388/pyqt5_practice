import asyncio


# @asyncio.coroutine 把一个 generator 标记为 coroutine 类型
@asyncio.coroutine
def hello():
    print('Hello world')

    # asy invoke asynio.sleep(1)
    # asyncio.sleep(1)看成是一个耗时2秒的IO操作，在此期间，主线程并未等待，
    # 而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
    r = yield from asyncio.sleep(2)
    print('Hello Again')


# create/subcalss a loop obj
loop = asyncio.get_event_loop()

# exec the coroutine
loop.run_until_complete(hello())
# close it
loop.close()