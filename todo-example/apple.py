class Apple_pie(object):
    def __init__(self):
        self._import_errors = {}

    def test(self):
        self.qqq = 'hi'
        return self.qqq


apple_pie = Apple_pie()
res = apple_pie.test()
print(res)
