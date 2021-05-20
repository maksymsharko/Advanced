import random
from abc import ABC, abstractmethod


class Animal:
    """
    Parent class, should have eat, sleep
    """

    def __init__(self, name):
        self._name = name

    def eat(self):
        print(f"{self._name} eat something")

    def sleep(self):
        print(f"{self._name} is sleeping")


class Cat(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def do_nothing(self):
        print(f"{self._name} is a cat and it is doing nothing")


class Horse(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def run(self):
        print(f"Horse {self._name} running")


class Chicken(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def lay_egg(self):
        print(f"Egg")


class Cow(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def graze(self):
        print(f"Cow {self._name} grazing")


class Monkey(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def calculate_sum(self, *args):
        res = sum(args)
        res += random.randint(0, int(res))
        print(f"Sum of {args} is {res}")

    def learn_english(self):
        print(f"My is {self._name} name")


def task1():
    cat = Cat("Peach")
    horse = Horse("Przewalski")
    chicken = Chicken(124)
    cow = Cow("Milka")
    monkey = Monkey("Rozetta")
    cat.do_nothing()
    horse.run()
    chicken.lay_egg()
    cow.graze()
    monkey.learn_english()
    monkey.calculate_sum(5, 2, 10, 53, 17, 3, 9)
    for animal in (cat, horse, chicken, cow, monkey):
        print(isinstance(animal, Animal))


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
# create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def __init__(self, name):
        self._name = name

    def eat(self):
        print(f"{self._name} eat apple")

    def sleep(self):
        print(f"{self._name} is sleeping in own home")

    def study(self):
        print(f"{self._name} is studying")

    def work(self):
        print(f"{self._name} pretends to work")


class Centaur(Horse, Human):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def read(self):
        print(f"{self._name} reading")


def task1a():
    centaur = Centaur("Pholus")
    centaur.run()
    centaur.read()
    centaur.work()
    centaur.study()
    centaur.sleep()
    centaur.eat()


# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.
class Person:
    """
    Make the class with composition.
    """

    def __init__(self):
        self.arms = (Arm(), Arm())


class Arm:
    """
    Make the class with composition.
    """
    pass


# b.
class Screen:
    """
    Make the class with aggregation
    """
    pass


class CellPhone:
    """
    Make the class with aggregation
    """

    def __init__(self, screen: Screen):
        self.screen = screen


# 3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        return str(list(self.__dict__.values()))


# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def web_cam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def screen(self):
        print("HPScreen")

    def keyboard(self):
        print("HPKeyboard")

    def touchpad(self):
        print("HPTouchpad")

    def web_cam(self):
        print("HPWebCam")

    def ports(self):
        print("HPPorts")

    def dynamics(self):
        print("HPDynamics")

if __name__ == "__main__":
    task1()
    print()
    task1a()