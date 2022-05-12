from collections import namedtuple

Person = namedtuple("Person", "name age height weight")
person = Person("James", "99", "178cm", "Too Much!")

print(person)

print(f"""
    --- Named Tuple Example ---
    > Name: {person.name}
    > Age: {person.age}
    > Height: {person.height}
    > Weight: {person.weight}
""")
