# https://www.liaoxuefeng.com/wiki/1016959663602400/1017985577429536

# 由於HTTP連接就是IO操作，因此可以用 `單線程 + coroutine` 實現多用戶的高並發支持
# asyncio實現了TCP、UDP、SSL等協議，aiohttp則是基於asyncio實現的HTTP框架。


""" 
編寫一個HTTP服務器，分別處理以下URL：

/ 
首頁返回b'<h1>Index</h1>'；

/hello/{name}  
根據URL參數返回文本hello, %s!。 

"""



import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = f'<h1> Hello! {request.match_info["name"]}</h1>'
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    server_ = await loop.create_server(app.make_handler(),'127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000.....')
    return server_


# create/subcalss a loop obj
loop = asyncio.get_event_loop()


# exec the coroutine
loop.run_until_complete(init(loop))

# keep it running until manual stop
loop.run_forever()
