# https://www.liaoxuefeng.com/wiki/1016959663602400/1017968846697824

# conrountine函數是一個generator
def conrountine():

    r = ''

    while True:

        # 通過yield拿到消息，處理，又通過yield把結果傳回
        n = yield r
        if not n:
            return
        print(f'[conrountine] running {n}...')
        r = '200 OK'


def Manager(c):

    # 調用c.send(None)啟動生成器
    c.send(None)

    n = 0
    while n < 5:
        n = n + 1
        print(f'[Manager] managing {n}...')
        # 通過c.send(n)切換到conrountine執行
        r = c.send(n)
        print(f'[Manager] conrountine return: {n}')

    # 通過c.close()關閉conrountine，整個過程結束
    c.close()

c = conrountine()
Manager(c)