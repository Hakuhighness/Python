"""
面向对象 - 多态
"""


class Animal:
    name = "Animal"
    age = 0

    def make_sound(self):
        print("动物发音")


class Dog(Animal):
    def make_sound(self):
        print("汪汪")


class Cat(Animal):
    def make_sound(self):
        print("喵喵")


animal: Animal = Animal()
animal.make_sound()

print("")

dog: Animal = Dog()
dog.make_sound()

print("")

cat: Animal = Cat()
cat.make_sound()

