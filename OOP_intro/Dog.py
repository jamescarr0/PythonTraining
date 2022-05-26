class Dog:
    ''' Class attribute demo '''
    species = 'mammal'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


diesel = Dog('Diesel', 10)
scooby = Dog('Scooby', 13)

Dog.species = 'unknown'
scooby.species = 'mammal'

if scooby.species == 'mammal':
    print(f"{scooby.name} is a {scooby.species}")

if diesel.species == 'mammal':
    print(f"{diesel.name} is a {diesel.species}")

print(f"Class attribute is: {Dog.species}")
