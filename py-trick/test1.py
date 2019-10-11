from collections import namedtuple

# Car = namedtuple('Car', 'color mile')

Car = namedtuple('Car', [
    'color',
    'mile'
])

my_car = Car('red', 42)


# print(my_car.color)
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return 'red!!'
        else:
            return 'not red'

c = MyCarWithMethods('red', 2233)
print(c.hexcolor())

ElectricCar = namedtuple('ElectricCar', Car._fields+('charge',))

# print(ElectricCar('red', 1233, 12.0))

import json
print(json.dumps(my_car._asdict()))








