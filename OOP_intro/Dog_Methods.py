class Dog:
    ''' Class attribute demo '''
    species = 'mammal'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def birthday(self):
        self.age += 1

diesel = Dog('Diesel', 10)
scooby = Dog('Scooby', 13)

print(diesel.description())
print(diesel.speak("Woof Woof, grrrrr!!"))
