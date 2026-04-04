from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        pass

class Lion(Animal):
    def make_noise(self):
        print("Roar")

class Cat(Animal):
    def make_noise(self):
        print("Meow")

class Cow(Animal):
    def make_noise(self):
        print("Moo")

cow = Cow()
cow.make_noise()
cat = Cat()
cat.make_noise()
lion = Lion()
lion.make_noise()