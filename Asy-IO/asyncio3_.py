# https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640

import asyncio


@asyncio.coroutine
def wget(host):
    
    print(f'wget {host}...')


    connect = asyncio.open_connection(host,80)
    reader, writer = yield from connect

    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode('utf-8'))
    yield from writer.drain()

    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print(f"{host} header > {line.decode('utf-8').rstrip()}")

    writer.close()

    
# create/subcalss a loop obj
loop = asyncio.get_event_loop()

# 用Task封装3个coroutine
tasks = [wget(host) for host in ['www.sina.com.cn',
                                'www.sohu.com',
                                'www.163.com']]

# exec the coroutine
loop.run_until_complete(asyncio.wait(tasks))

# close it
loop.close()
