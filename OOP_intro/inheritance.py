class Person:
    description = "general person"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and i am {self.age} years old")

    def eat(self, food):
        print(f"{self.name} easts {food}, nom nom.")

    def action(self):
        print(f"{self.name} performs some exercise, urghh")


class Baby(Person):
    description = "baby"

    def speak(self):
        ''' Overrides the parent speak method '''
        print("ba ba ba ba ba")

    def nap(self):
        print(f"{self.name} takes a nap, ZZZzzzzzz..")

print("-"*20)
person = Person("James", 99)
person.speak()
person.eat("chips")
person.action()

print("-"*20)

baby = Baby("Alfie", 3)
baby.speak()
baby.eat("Mushed broccoli")
baby.action()

print("-"*20)

print(f"Baby is an instance of type Person?: {isinstance(baby, Person)}")
# Everything in python inherits object.
print(f"Baby is an instance of type Object?: {isinstance(baby, object)}")
print(f"Baby is an instance of type Baby?: {isinstance(baby, Baby)}")
print("-"*20)