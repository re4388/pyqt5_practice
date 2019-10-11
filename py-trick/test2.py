class Dog:
    numbers_leg = 4
    def __init__(self,name):
        self.name = name

Jack = Dog('Jack')
Jill = Dog('Jill')

# print(Jack.name, Jill.name)
# print(Jack.numbers_leg, Jill.numbers_leg)
# print(Dog.name)

Dog.numbers_leg = 6
print(Jack.numbers_leg, Jill.numbers_leg)


