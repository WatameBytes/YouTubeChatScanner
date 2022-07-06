class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

# Rabbit is the child class while ANIMAL is the parent class
class Rabbit(Animal):
    def run(self):
        print("This animal is running!")

class Fish(Animal):
    pass


rabbit = Rabbit()
fish = Fish()

rabbit.eat()
rabbit.run()