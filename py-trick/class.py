# class MyClass:

#     def method(self):
#         return 'instance method call', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method called'


# obj = MyClass()
# x = obj.method()
# print(x)

# print(MyClass.method(obj))
# print(obj.classmethod())
# print(obj.staticmethod())


# print(MyClass.method())
# print(MyClass.classmethod())
# print(MyClass.staticmethod())


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'

#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])

#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzrella', 'tomotoes', 'ham'])


# print(Pizza.margherita())
# print(Pizza.prosciutto())


# x = Pizza(['cheese', 'tomotoes'])
# print(x)


import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}),' f'{self.ingredients!r}')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return 2 * math.pi ** r


pizza = Pizza(4, ['mozzarella', 'tomatoes'])
print(pizza)

print(pizza.area())
print(Pizza.circle_area(4))
